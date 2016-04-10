import cv2


def find_bottle():
    img = cv2.imread('parachute3.jpg')
    e1 = cv2.getTickCount()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255,
                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow("Thresh", thresh)
    res = cv2.bitwise_and(gray, gray, mask=thresh)
    # cv2.imwrite("thresh3.jpg", thresh)
    cv2.imwrite("Res2.jpg", res)
    ret, thresh2 = cv2.threshold(res, 0, 255,
                                 cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # cv2.imshow("Img", img)
    cv2.imshow("Thresh2", thresh2)
    res = cv2.bitwise_and(res, res, mask=thresh2)
    cv2.imshow("REs", res)
    (_, cnts, _) = cv2.findContours(res, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area < 5 or area > 50:
            # print area
            continue
        else:
            print area
        cv2.putText(img, str(area), (x+w, y+h),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255))
    # cv2.drawContours(img, cnts, -1, (0, 255, 0))
    cv2.imshow("Final", img)
    e2 = cv2.getTickCount()
    time = (e2 - e1) / cv2.getTickFrequency()
    print time
    cv2.imwrite("final1.jpg", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    find_bottle()
