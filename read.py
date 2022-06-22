import cv2 as cv
#import winsound #for windows
import playsound #for mac

capture = cv.VideoCapture(0)
file = "alert.wav"

while capture.isOpened():
    ret, frame = capture.read()
    ret, frame2 = capture.read()

    comp = cv.absdiff(frame, frame2)
    gray = cv.cvtColor(comp, cv.COLOR_RGB2GRAY)
    blur1 = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur1, 20,255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(frame,contours,-1,(0,255,0),2)
    for x in contours:
        if cv.contourArea(x) <5000:
            continue
        x,y,w,h = cv.boundingRect(x)
        cv.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        #winsound.PlaySound('alert.wav', winsound.SND_ASYNC) #for windows
        playsound.playsound('alert.wav', block=False) #formac

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()