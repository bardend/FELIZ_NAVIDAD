import numpy, cv2, sys
import Tools

stream = cv2.VideoCapture('video.mp4')

while (stream.isOpened()):
    ret, frame = stream.read()
    if (ret == False): # finished all frames
        break

    frame = Tools.segment(frame, 20)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
