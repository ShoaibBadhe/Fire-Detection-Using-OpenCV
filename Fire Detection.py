import cv2
from playsound import playsound

fireCascade = cv2.CascadeClassifier('fire_detection.xml')

#used ip-webcam application when running through mobile
video = cv2.VideoCapture(0)
address = 'http://IPADDRESS/video'
video.open(address)

while True:
    flag,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire = fireCascade.detectMultiScale(gray,1.1,5)
    for x,y,w,h in fire:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(frame,'Fire',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        print('Fire Detected,Bhaag Beta')
        playsound('audio.mp3')
    cv2.imshow('Fire Detection',frame)
    cv2.waitKey(1)
