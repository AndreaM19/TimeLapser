# Time-Lapser Python script

import time
import picamera
import os

# Time between two frames (second)
frame_interval=eval(input('Intervallo di scatto (Secondi): '))
# Video Hours
video_hours=eval(input('Durata del video (ore): '))
# Folder name - contains captured frames
folder=input('Nome cartella in cui salvare le immagini: ')
directory='/home/pi/projects/TimeLapser/%s' % folder;

frames=int(((60*60)/frame_interval)*video_hours)

if not os.path.exists(directory):
    os.makedirs(directory)

# Function capture_frame
def capture_frame(frameId):
    time.sleep(2)
    camera.capture('%s/frame%03d.jpg' % (folder, frameId))
    print('Frame saved in %s/frame%03d.jpg' % (folder, frameId))
# End of function

# Capture the images
x=1
for frameId in range(frames):
    # Note the time before the capture
    print('Capturing image %d...' % x)
    camera=picamera.PiCamera()
    x=x+1
    capture_frame(frameId)
    camera.close()
    # Wait for the next capture
    time.sleep(frame_interval-2)
