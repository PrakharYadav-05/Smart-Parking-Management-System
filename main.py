import cv2
import pickle
import numpy as np
from utils import check_parking_space

# Video feed
cap = cv2.VideoCapture('parking_video.mp4')

# Load parking space positions
try:
    with open('CarParkPos', 'rb') as f:
        pos_list = pickle.load(f)
except FileNotFoundError:
    pos_list = []

width, height = 107, 48

def main():
    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = cap.read()
        if not success:
            break

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
        img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        img_median = cv2.medianBlur(img_threshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        img_dilate = cv2.dilate(img_median, kernel, iterations=1)

        free_spaces, img_annotated = check_parking_space(img_dilate, pos_list, width, height)

        # Show original image with annotations
        # Note: In a real environment, we would use cv2.imshow
        # For this simulation, we'll just process the frames.
        
        # cv2.imshow("Image", img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
