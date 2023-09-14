import cv2


def apply_gaussian_blur(frame_, kernel_size=(5, 5)):
    return cv2.GaussianBlur(frame_, kernel_size, 0)


def apply_clahe(frame_, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab = cv2.cvtColor(frame_, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    cl = clahe.apply(l)
    img = cv2.merge((cl, a, b))
    final = cv2.cvtColor(img, cv2.COLOR_Lab2BGR)
    return final
