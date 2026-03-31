import cv2
import numpy as np
import os

def create_parking_image(path, width=1100, height=720):
    # Create a gray background (asphalt)
    img = np.ones((height, width, 3), dtype=np.uint8) * 50
    
    # Draw parking lines
    # Let's draw two rows of parking spots
    spot_w, spot_h = 107, 48
    start_x, start_y = 50, 100
    
    # Row 1
    for i in range(8):
        x = start_x + i * (spot_w + 10)
        y = start_y
        cv2.rectangle(img, (x, y), (x + spot_w, y + spot_h), (200, 200, 200), 2)
        
    # Row 2
    start_y_2 = 300
    for i in range(8):
        x = start_x + i * (spot_w + 10)
        y = start_y_2
        cv2.rectangle(img, (x, y), (x + spot_w, y + spot_h), (200, 200, 200), 2)
        
    cv2.imwrite(path, img)
    print(f"Created {path}")

def create_parking_video(path, img_path, frames=100):
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path, fourcc, 10.0, (width, height))
    
    spot_w, spot_h = 107, 48
    start_x, start_y = 50, 100
    start_y_2 = 300
    
    # Define some "cars" (colored rectangles)
    # (row, index, color)
    cars = [
        (0, 0, (0, 0, 255)), # Red car
        (0, 2, (255, 0, 0)), # Blue car
        (1, 1, (0, 255, 0)), # Green car
        (1, 5, (255, 255, 255)) # White car
    ]
    
    for f in range(frames):
        frame = img.copy()
        # Add some noise to simulate real video
        noise = np.random.randint(0, 10, (height, width, 3), dtype=np.uint8)
        frame = cv2.add(frame, noise)
        
        # Draw cars
        for row, idx, color in cars:
            x = start_x + idx * (spot_w + 10) + 5
            y = (start_y if row == 0 else start_y_2) + 5
            # Draw a car-like shape
            cv2.rectangle(frame, (x, y), (x + spot_w - 10, y + spot_h - 10), color, -1)
            
        out.write(frame)
        
    out.release()
    print(f"Created {path}")

if __name__ == "__main__":
    img_file = "/home/ubuntu/smart-parking-management/carParkImg.png"
    video_file = "/home/ubuntu/smart-parking-management/parking_video.mp4"
    create_parking_image(img_file)
    create_parking_video(video_file, img_file)
