import cv2


# Function to find the current blobs in the frame
def find_current_blobs(bin_image, area_threshold=500):
    contours, _ = cv2.findContours(bin_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    __current_centers = []
    for contour in contours:

        if cv2.contourArea(contour) < area_threshold:
            continue

        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            __current_centers.append((cX, cY))
    return __current_centers


def motion_detection(frame_, previous_frame_):
    diff = cv2.absdiff(previous_frame_, frame_)
    grayscale = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(grayscale, 25, 255, cv2.THRESH_BINARY)
    return threshold
