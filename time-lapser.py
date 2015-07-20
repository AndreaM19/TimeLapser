# Time-Lapser Python script

import time
import picamera
import os

# 3=one frame every 20 minutes
# 6=one frame every 10 minutes
# 12=one frame every 5 minutes
# 24=one frame every 2.5 minutes
#FRAMES_PER_HOUR=3
#VIDEO_HOURS=1

directory='/home/pi/projects/TimeLapser/test-2';

#FRAMES=FRAMES_PER_HOUR * VIDEO_HOURS

#Time between two frames (second)
FRAME_PERIOD=10
VIDEO_HOURS=1
FRAMES=int(((60*60)/FRAME_PERIOD)*VIDEO_HOURS)

camera=picamera.PiCamera()

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
    start = time.time()
    print('Capturing image %d...' % x)
    x=x+1
    capture_frame(frame)
    # Wait for the next capture. Note that we take into
    # account the length of time it took to capture the
    # image when calculating the delay
    #if VIDEO_HOURS==1 and FRAMES_PER_HOUR==1:
    #    waiting_time = 1
    #else:
    #    waiting_time = int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
    time.sleep(FRAME_PERIOD-2)
