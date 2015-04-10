#Time-Lapser Python script

import time
#import picamera

#VIDEO_DAYS = 1
FRAMES_PER_HOUR = 1
VIDEO_HOURS=1
# FRAMES define the number of frame captured from the camera 
FRAMES = FRAMES_PER_HOUR * VIDEO_HOURS


# Function capture_frame
def capture_frame(frame):
    #with picamera.PiCamera() as cam:
        time.sleep(2)
        #cam.capture('test-1/frame%03d.jpg' % frame)
        print('Frame saved in test-1/frame%03d.jpg' % frame)
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
    if VIDEO_HOURS==1 and FRAMES_PER_HOUR==1:
        waiting_time = 1
    else:
        waiting_time = int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
    time.sleep(waiting_time)
