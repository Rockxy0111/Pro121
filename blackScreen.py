import cv2
import numpy as np

video = cv2.VideoCapture(0)

image = cv2.imread("Buddha Statue.jpg")


while (video.isOpened()):

    ret, frame = video.read()


    image = cv2.resize(image, (640, 480))
    frame = cv2.resize(frame, (640, 480))

    
    upper_black = np.array([104, 153, 70])
    lower_black = np.array([30, 30, 0])

    mask = cv2.inRange(frame, lower_black, upper_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    output = cv2.addWeighted(f, 1, image, 0, 0)

    cv2.imshow("background", output)
    key = cv2.waitKey(1)

    if key & 0xFF == 27:
        break
    if key & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()