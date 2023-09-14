import cv2


def draw_min_enclosing_circles(bin_image, original_image, area_threshold=3000):
    contours, _ = cv2.findContours(bin_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Get the area of contour, if it is less than some value consider it as noise and ignore
        if cv2.contourArea(contour) < area_threshold:
            continue

        # Draw the bounding circle
        (x, y), radius = cv2.minEnclosingCircle(contour)
        curr_center = (int(x), int(y))
        radius = int(radius)
        if radius > 5:
            cv2.circle(original_image, curr_center, radius, (0, 255, 0), 2)

    return original_image



