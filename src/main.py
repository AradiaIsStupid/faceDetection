import cv2

faceCas = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)
address= "http://192.168.1.8:8080/video"
video.open(address)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceCas.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors= 5)
    for x,y,w,h in face:
        img = cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,255), 3) 
        cv2.putText(img, 'massive retard', (x, y-10), cv2.FONT_HERSHEY_COMPLEX,0.9,(0,255,255), 2)
    cv2.imshow("idk what i am doing anymore", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows
