import os
import cv2

videos_save_path = 'C:\\Users\\USER\\Desktop\\USBWebcameSave'
each_video_name = "USBWebcameSave"

cap  = cv2.VideoCapture(0)
frame_count = 1
success = True
while(success):
        success, frame = cap.read()
        cv2.imshow("Window", frame)
        k = cv2.waitKey(1)
        print('Read a new frame: ', success)
        params = []
        params.append(cv2.IMWRITE_PXM_BINARY)
        params.append(1)
        cv2.imwrite("C:\\Users\\USER\\Desktop\\20180904USBWebcameSave\\USBWebCam%d.jpg" % frame_count, frame, params)

        frame_count = frame_count + 1

cap.release()
cv2.destroyWindow("Window")