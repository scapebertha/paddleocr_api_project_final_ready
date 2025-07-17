
import cv2

def resize_if_large(img, max_width=1200):
    height, width = img.shape[:2]
    if width > max_width:
        scale_ratio = max_width / width
        img = cv2.resize(img, (int(width * scale_ratio), int(height * scale_ratio)))
    return img
