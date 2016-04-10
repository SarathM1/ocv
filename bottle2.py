import cv2
import numpy as np


def find_bottle():
    img = cv2.imread('parachute3.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255,
                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    (_, cnts, _) = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(c) for c in cnts]
    index = np.argmax(areas)
    cnt = cnts[index]
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.circle(img, (x, y), 1, (150, 0, 0), 4)
    cv2.circle(img, (x+w, y+h), 1, (0, 0, 150), 4)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))

    # bottle = img[y:y+h, x:x+w]
    x1 = (x+w/2) + 50
    x2 = x+w
    y1 = y+h/2
    y2 = y+h-50
    label = img[y1:y2, x1:x2]
    cv2.imwrite("label.jpg", label)
    label_hsv = cv2.cvtColor(label, cv2.COLOR_BGR2HSV)
    blue_low = np.array([107, 50, 50], np.uint8)
    blue_high = np.array([112, 255, 255], np.uint8)
    thresh = cv2.inRange(label_hsv, blue_low, blue_high)
    cv2.imshow("Label", label)
    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)

if __name__ == '__main__':
    find_bottle()
