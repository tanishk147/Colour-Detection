import cv2
from PIL import Image
from util import get_limits

# Colors in RGB colorspace
yellow = [0, 255, 255]  # Yellow
red = [255, 0, 0]       # Red
blue = [0, 0, 255]      # Blue
green = [0, 255, 0]     # Green

# Open the first camera device (camera index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Mirror the frame horizontally
    frame = cv2.flip(frame, 1)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV limits for each color
    yellow_limits = get_limits(yellow)
    red_limits = get_limits(red)
    blue_limits = get_limits(blue)
    green_limits = get_limits(green)

    # Create yellow mask
    yellow_mask = cv2.inRange(hsvImage, *yellow_limits[0])
    yellow_mask2 = cv2.inRange(hsvImage, *yellow_limits[1])
    yellow_mask = cv2.bitwise_or(yellow_mask, yellow_mask2)

    # Create masks for other colors
    red_mask = cv2.inRange(hsvImage, *red_limits[0])
    red_mask = cv2.bitwise_or(red_mask, cv2.inRange(hsvImage, *red_limits[1]))
    blue_mask = cv2.inRange(hsvImage, *blue_limits)
    green_mask = cv2.inRange(hsvImage, *green_limits)

    # Combine masks
    combined_mask = cv2.bitwise_or(yellow_mask, cv2.bitwise_or(red_mask, cv2.bitwise_or(blue_mask, green_mask)))

    # Convert combined mask to PIL image to get bounding box
    mask_ = Image.fromarray(combined_mask)
    bbox = mask_.getbbox()

    # Draw bounding box on frame
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    print(bbox)

    # Display frame with bounding box
    cv2.imshow('frame', frame)

    # Check for exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
