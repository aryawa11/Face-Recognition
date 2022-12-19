# import required libraries
import cv2

# read the input image
cap = cv2.VideoCapture(0)

# read the haarcascade to detect the faces in an image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    #Capture frame by frame
    ret, frame = cap.read()

    # convert to grayscale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detects faces in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    print('Number of detected faces:', len(faces))

    # loop over all detected faces
    # if len(faces) > 0:
    #     for i, (x, y, w, h) in enumerate(faces):

    #         # To draw a rectangle in a face
    #         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    #         face = frame[y:y + h, x:x + w]
    #         cv2.imshow("Cropped Face", face)
    #         cv2.imwrite(f'face{i}.jpg', face)
    #         print(f"face{i}.jpg is saved")

    # display the image with detected faces
    cv2.imshow("image", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()