import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
class VideoCamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture("rtsp://admin:admin1234@192.168.1.15:554/cam/realmonitor?channel=1&subtype=0")
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            break
        ret,jpeg=cv2.imencode('.jpg',frame)
        return jpeg.tobytes()
