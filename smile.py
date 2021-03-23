import cv2
smile_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# webcam
webcam = cv2.VideoCapture()

# show current frame
while True:
    success_frame_read, frame = webcam.read()

    # if error abort
    if not success_frame_read:
        break

    # show current frame
    cv2.imshow('smile', frame)

    # display
    cv2.waitKey(1)

# cleanUp
webcam.release()
cv2.destroyAllWindows()
