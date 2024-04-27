
#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera2 import Picamera2, Preview
import time
from signal import pause

#create objects that refer to a button,
#a motion sensor and the PiCamera
button = Button(2)
pir = MotionSensor(4)
picam2 = Picamera2()

#init the camera
# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.
camera_config = picam2.create_preview_configuration(main={"size": (1000, 800)})
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)

#image image names
i = 0

#stop the camera when the pushbutton is pressed
def stop_camera():
    picam2.stop_preview()
    picam2.close()
    #exit the program
    exit()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    picam2.capture_file('/home/everyways/Desktop/image_%s.jpg' % i)
    print('A photo has been taken')
    time.sleep(10)

#assign a function that runs when the button is pressed
button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo

pause()