import cv2
import numpy as np

def check_parking_space(img, pos_list, width, height):
    """
    Checks if parking spaces are occupied or vacant.
    :param img: The image to check.
    :param pos_list: List of parking space positions.
    :param width: Width of each parking space.
    :param height: Height of each parking space.
    :return: Count of free spaces and the annotated image.
    """
    space_counter = 0
    for pos in pos_list:
        x, y = pos
        img_crop = img[y:y + height, x:x + width]
        count = cv2.countNonZero(img_crop)

        if count < 900:  # Threshold for vacancy
            color = (0, 255, 0)
            thickness = 5
            space_counter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, (x, y), (x + width, y + height), color, thickness)
        cv2.putText(img, str(count), (x, y + height - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv2.putText(img, f'Free: {space_counter}/{len(pos_list)}', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return space_counter, img
