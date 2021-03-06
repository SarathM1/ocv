import cv2
import numpy as np


def find_bottle():
    img = cv2.imread('parachute3.jpg')
    e1 = cv2.getTickCount()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255,
                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    (_, cnts, _) = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(c) for c in cnts]
    index = np.argmax(areas)
    cnt = cnts[index]
    x, y, w, h = cv2.boundingRect(cnt)

    # bottle = img[y:y+h, x:x+w]
    x1 = (x+w/2) + 50
    x2 = x+w
    y1 = y+h/2
    y2 = y+h-50
    label = img[y1:y2, x1:x2]
    cv2.imshow("Label", label)

    gray = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 15)

    kernel = np.ones((5, 5), np.uint8)
    cv2.dilate(thresh, kernel, iterations=1)
    cv2.imshow("thresh", thresh)
    (_, cnts, _) = cv2.findContours(thresh, cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(label, cnts, -1, (0, 0, 255), 1)
    img[y1:y2, x1:x2] = label
    e2 = cv2.getTickCount()
    time = (e2 - e1) / cv2.getTickFrequency()
    print "Completed in : ", time, " secs"
    cv2.imshow("Final", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    find_bottle()
