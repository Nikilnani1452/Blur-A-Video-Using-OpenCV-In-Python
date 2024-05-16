import cv2
import numpy as np

capt = cv2.VideoCapture('videos/InputVideo.mp4')

if not capt.isOpened():
    print('An Error occurred while opening! Kindly check again.')

frame_width = int(capt.get(3))
frame_height = int(capt.get(4))
result = cv2.VideoWriter('videos/BlurredVideo.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width, frame_height))

while capt.isOpened():
    ret, frame = capt.read()
    if ret:
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        result.write(frame)
        cv2.imshow('Video', frame)
        if cv2.waitKey(27) & 0xFF == ord('e'):
            break
    else:
        break

capt.release()
result.release()  # Don't forget to release the result VideoWriter
cv2.destroyAllWindows()