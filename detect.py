import cv2

from pathlib import Path

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

vc = cv2.VideoCapture(0)

print("Enter user id and name: ")
userId=input()
userName=input()
count=1

def saveImage(img, userId, userName, imgId):
    Path("dataset/{}".format(userName)).mkdir(parents=True, exist_ok=True)
    cv2.imwrite("dataset/{}/{}_{}.jpg".format(userName, userId, imgId),img)

while True:

    _, img = vc.read()

    originalImg = img

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces= faceCascade.detectMultiScale(gray_img, scaleFactor=1.2,minNeighbors=5,minSize=(50,50))

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        coords = [x,y,w,h]

    cv2.imshow("identified faces", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        if count<=5:
            roi_img = originalImg[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
            saveImage(roi_img, userId, userName, count)
            count += 1
        else:
            break
    elif key == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()
