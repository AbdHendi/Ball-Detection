import time
from skimage.exposure import is_low_contrast
from processing import apply_clahe, apply_gaussian_blur
from blob import Blob
from utils import draw_min_enclosing_circles
import numpy as np
from ball_detection import *

prev_centers = []
all_blobs = []
bounces = 0
cap = cv2.VideoCapture('test/video.mp4')

ret, previous_frame = cap.read()
previous_frame = cv2.resize(previous_frame, (410, 615))
if is_low_contrast(previous_frame):
    previous_frame = apply_clahe(previous_frame)

print("Start Video ")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    frame = cv2.resize(frame, (410, 615))

    if is_low_contrast(frame):
        frame = apply_clahe(frame)

    frame = apply_gaussian_blur(frame)
    motion = motion_detection(frame, previous_frame)
    cv2.imshow('Motion', motion)

    # Using the motion mask to get the moving parts of the frame
    moving_parts = cv2.bitwise_and(frame, frame, mask=motion)
    current_centers = find_current_blobs(motion)

    # Associate current centers with blobs or create new blobs
    if not all_blobs:
        for center in current_centers:
            blob = Blob()
            blob.add(center)
            all_blobs.append(blob)
    else:
        for center in current_centers:
            matched = False
            for blob in all_blobs:
                if np.linalg.norm(np.array(center) - np.array(blob.centers[-1])) < 600:  # Threshold may need tweaking
                    blob.add(center)
                    matched = True
                    break
            if not matched:
                blob = Blob()
                blob.add(center)
                all_blobs.append(blob)

    if all_blobs and len(all_blobs[0].centers) >= 30:

        max_speed = -1
        max_spread = -1
        ball_blob = None
        for blob in all_blobs:
            speed = blob.compute_speed()
            spread = blob.compute_spread()
            if speed > max_speed and spread > max_spread and speed > 20 and spread > 30:
                ball_blob = blob
                max_speed = speed
        if ball_blob:
            cv2.circle(frame, ball_blob.centers[-1], 5, (0, 255, 0), -1)  # Marking the ball
            # if ball_blob.detect_bounce(): bounces += 1 cv2.putText(frame, "Bounces: " + str(bounces), (10, 20),
            # cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow('Frame', frame)
    time.sleep(0.02)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    previous_frame = frame

cap.release()
cv2.destroyAllWindows()
