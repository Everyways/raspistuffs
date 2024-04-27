
#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera2 import Picamera2, Preview
from time import sleep
from signal import pause

#create objects that refer to a button,
#a motion sensor and the PiCamera
button = Button(2)
pir = MotionSensor(4)
picam2 = Picamera2()

#start the camera
picam2.rotation = 180
picam2.start_preview()

#image image names
i = 0

#stop the camera when the pushbutton is pressed
def stop_camera():
    picam2.stop_preview()
    #exit the program
    exit()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    picam2.start_and_record_video('/home/everyways/Desktop/image_%s.jpg' % i, duration=5)
    print('A photo has been taken')
    sleep(10)

#assign a function that runs when the button is pressed
button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo

pause()