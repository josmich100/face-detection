import cv2
from random import randrange
#loading dataset
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#choose an image to detect faces in 
#img=cv2.imread('cool.png')

#capture video
webcam = cv2.VideoCapture(0)

#iterate forever over frames
while True:
    
    ###Read the current frame
    successful_frame_read,frame = webcam.read()
    
    #must convert grayscale
    grayscaled_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Draw rectangles
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame,(x, y),(x+w, y+h),(randrange(256),0,0),2)
    
    cv2.imshow('kanyama',frame)
    key= cv2.waitKey(1)
    
    #quit ASCII
    if key==81 or key==113:
        break
    
    #release
webcam.release()


"""
#must convert grayscale
grayscaled_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
print(face_coordinates)

#Draw rectangles
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img,(x, y),(x+w, y+h),(randrange(256),0,0),2)

#print(faces_cordinates)

cv2.imshow('Kwamboka', img)

#show image
cv2.waitKey()
print('code')
"""