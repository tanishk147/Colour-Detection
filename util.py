import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    if color == [0, 255, 255]:  # Yellow
        lowerLimit1 = np.array([hsvC[0][0][0] - 10, 100, 100], dtype=np.uint8)
        upperLimit1 = np.array([hsvC[0][0][0] + 10, 255, 255], dtype=np.uint8)
        lowerLimit2 = np.array([hsvC[0][0][0] + 170, 100, 100], dtype=np.uint8)
        upperLimit2 = np.array([180, 255, 255], dtype=np.uint8)
        return (lowerLimit1, upperLimit1), (lowerLimit2, upperLimit2)
    elif color == [255, 0, 0]:  # Red
        lowerLimit1 = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit1 = np.array([10, 255, 255], dtype=np.uint8)
        lowerLimit2 = np.array([170, 100, 100], dtype=np.uint8)
        upperLimit2 = np.array([180, 255, 255], dtype=np.uint8)
        return (lowerLimit1, upperLimit1), (lowerLimit2, upperLimit2)
    elif color == [0, 255, 0]:  # Green
        lowerLimit = np.array([36, 100, 100], dtype=np.uint8)
        upperLimit = np.array([86, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit
    elif color == [0, 0, 255]:  # Blue
        lowerLimit = np.array([100, 100, 100], dtype=np.uint8)
        upperLimit = np.array([140, 255, 255], dtype=np.uint8)
        return lowerLimit, upperLimit
    else:
        return None, None  # Invalid color
