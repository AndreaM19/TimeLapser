# Time-Lapser Python script

import time
import picamera
import os

directory='/home/pi/projects/TimeLapser/test-2';

#Time between two frames (second)
FRAME_PERIOD=20
VIDEO_HOURS=1
FRAMES=int(((60*60)/FRAME_PERIOD)*VIDEO_HOURS)

#camera=picamera.PiCamera()

if not os.path.exists(directory):
    os.makedirs(directory)

# Function capture_frame
def capture_frame(frame):
  time.sleep(2)
  camera.capture('test-2/frame%03d.jpg' % frame)
  print('Frame saved in test-2/frame%03d.jpg' % frame)
# End of function

# Capture the images
x=1
for frame in range(FRAMES):
    # Note the time before the capture
    print('Capturing image %d...' % x)
    camera=picamera.PiCamera()
    x=x+1
    capture_frame(frame)
    camera.close()
    # Wait for the next capture
    time.sleep(FRAME_PERIOD-2)
