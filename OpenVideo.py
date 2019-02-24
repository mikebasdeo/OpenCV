import cv2

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,640);
video.set(cv2.CAP_PROP_FRAME_HEIGHT,480);

while True:
    check, frame = video.read()
    cv2.imshow('Video window', frame)

    # press 'q' on keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()