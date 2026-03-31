# Project Report: Smart Parking Management System

## 1. Introduction
This report details the development of a Smart Parking Management System utilizing computer vision. The primary goal of this project is to efficiently monitor parking lot occupancy, providing real-time information on available parking spaces. This system addresses common challenges associated with traditional parking management, such as inefficient space utilization and driver frustration in locating vacant spots.

## 2. Problem Statement
Traditional parking systems often rely on manual observation or basic sensor technology, which can be inefficient, prone to errors, and lack real-time capabilities. Drivers frequently waste time searching for parking, leading to increased traffic congestion, fuel consumption, and environmental impact. For parking facility operators, optimizing space utilization and managing traffic flow are critical for operational efficiency and customer satisfaction. The problem, therefore, is to develop an automated, accurate, and real-time solution for monitoring parking space availability.

## 3. Solution Approach
The Smart Parking Management System employs computer vision to analyze video feeds of a parking lot. The core idea is to define specific regions of interest (ROIs) corresponding to individual parking spaces and then determine the occupancy status of each ROI. The system processes video frames through a series of image processing steps to enhance visibility and accurately differentiate between occupied and vacant spaces. The final output provides a visual representation of the parking lot with annotated spaces and a real-time count of free spots.

## 4. Technical Details

### 4.1. System Architecture
The system comprises three main components:
1.  **Parking Space Picker (`ParkingSpacePicker.py`)**: A utility for initial setup, allowing users to manually define the coordinates and dimensions of each parking space on a static image of the parking lot. These coordinates are serialized and saved for persistent use.
2.  **Main Processing Module (`main.py`)**: The central script that reads video frames, applies image processing, and calls the utility function to check parking space status.
3.  **Utility Functions (`utils.py`)**: Contains the `check_parking_space` function, which performs the core logic of determining occupancy for each defined parking spot.

### 4.2. Image Processing Pipeline
Each frame from the video feed undergoes the following steps:
1.  **Grayscale Conversion**: The color frame is converted to grayscale to simplify subsequent processing and reduce computational load.
2.  **Gaussian Blur**: A Gaussian blur is applied to smooth the image and reduce noise, which helps in more robust thresholding.
3.  **Adaptive Thresholding**: Adaptive Gaussian Thresholding is used to convert the grayscale image into a binary image. This method is effective because it calculates the threshold for small regions of the image, making it adaptable to varying lighting conditions across the parking lot. `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` and `cv2.THRESH_BINARY_INV` are used with block size 25 and constant 16.
4.  **Median Blur**: A median blur is applied to further reduce salt-and-pepper noise introduced during thresholding.
5.  **Dilation**: A dilation operation is performed using a 3x3 kernel. This helps to thicken the white regions (representing cars) in the binary image, making them more prominent and easier to count.

### 4.3. Occupancy Detection Logic
The `check_parking_space` function iterates through each predefined parking space ROI. For each ROI, it extracts a cropped section from the processed binary image. The number of non-zero pixels within this cropped section is counted. A predefined threshold (e.g., `count < 900`) is used to classify a space as vacant (if the count of white pixels is below the threshold) or occupied (if above). This threshold is determined empirically and can be adjusted based on the specific parking lot and lighting conditions.

### 4.4. Visual Feedback
Based on the occupancy status, a rectangle is drawn around each parking space: green for vacant and red for occupied. The count of non-zero pixels for each space and the total number of free spaces are displayed on the frame, providing immediate visual feedback.

## 5. Key Decisions and Challenges

### 5.1. Key Decisions
-   **OpenCV for Image Processing**: OpenCV was chosen due to its comprehensive set of image processing and computer vision functions, making it suitable for real-time video analysis.
-   **Manual ROI Selection**: For simplicity and direct control over parking space definitions, a manual picker tool was implemented. This allows for precise demarcation of parking spots, which is crucial for accurate detection.
-   **Adaptive Thresholding**: Instead of a global threshold, adaptive thresholding was selected to handle varying illumination across the parking lot, which is a common issue in outdoor environments.
-   **Pixel Count for Occupancy**: Using the count of non-zero pixels in the binary image as the primary metric for occupancy was a pragmatic choice for a basic implementation, offering a balance between simplicity and effectiveness.

### 5.2. Challenges Faced
-   **Environmental Factors**: Varying lighting conditions (sunlight, shadows, night-time), rain, and reflections can significantly impact the accuracy of image processing and thresholding. The current adaptive thresholding helps but might not be robust enough for all scenarios.
-   **Threshold Sensitivity**: The `count < 900` threshold for determining vacancy is highly sensitive to the size of the parking spaces, the camera angle, and the preprocessing steps. Fine-tuning this value is critical and often requires empirical testing.
-   **Vehicle Diversity**: Different vehicle sizes, colors, and types can affect how they appear in the binary image, potentially leading to misclassifications.
-   **Occlusion**: Partial occlusion of parking spaces by other vehicles or objects can lead to inaccurate occupancy detection.
-   **Lack of Real-time Display in Sandbox**: Due to the sandbox environment, `cv2.imshow` was commented out, preventing real-time visual debugging and demonstration. This necessitated a more thorough review of the code logic and reliance on simulated processing.

## 6. Results and Discussion
The developed system successfully processes video frames to identify and count free parking spaces. The `ParkingSpacePicker.py` tool provides an intuitive way to set up parking regions. The `main.py` script, in conjunction with `utils.py`, demonstrates the core functionality of a computer vision-based parking management system. While the current implementation provides a solid foundation, its accuracy is heavily dependent on the quality of the input video and the tuning of image processing parameters.

For a production-ready system, integrating more advanced object detection models (like YOLO) would significantly improve robustness against varying conditions and vehicle types. This would move beyond simple pixel counting to actual vehicle detection and tracking.

## 7. Conclusion
This project successfully demonstrates the application of fundamental computer vision techniques to solve a real-world problem: smart parking management. It highlights the importance of image preprocessing, ROI definition, and thresholding in achieving automated detection. While challenges related to environmental variability and detection robustness exist, the project provides a strong foundation for further enhancements and integration with more sophisticated AI models.

## References
-   [Ultralytics Blog: 10 easy computer vision projects for hands-on learning](https://www.ultralytics.com/blog/10-easy-computer-vision-projects-for-hands-on-learning) (Accessed: March 31, 2026)
