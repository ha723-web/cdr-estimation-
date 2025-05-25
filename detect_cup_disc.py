import cv2
import numpy as np

def detect_cup_disc(image_input):
    # Accept both file path or image array
    if isinstance(image_input, str):
        img = cv2.imread(image_input)
    else:
        img = image_input.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)

    circles = cv2.HoughCircles(
        blur, cv2.HOUGH_GRADIENT, 1, 100,
        param1=50, param2=30, minRadius=30, maxRadius=100
    )

    cdr = None
    if circles is not None and len(circles[0]) >= 2:
        sorted_circles = sorted(circles[0], key=lambda x: x[2])  # Sort by radius
        cup_radius = sorted_circles[0][2]
        disc_radius = sorted_circles[1][2]
        cdr = round(cup_radius / disc_radius, 2)

        # Draw circles
        for i in sorted_circles[:2]:
            center = (int(i[0]), int(i[1]))
            radius = int(i[2])
            color = (0, 255, 0) if radius == disc_radius else (0, 0, 255)
            cv2.circle(img, center, radius, color, 2)

        return img, cup_radius, disc_radius
    else:
        return img, None, None

