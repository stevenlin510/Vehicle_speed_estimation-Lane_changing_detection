import numpy as np
import cv2

video = cv2.VideoCapture('Highway - 56310.mp4')

FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=100)

#creating an array of frames from frames chosen above
frames = []

for frameOI in FOI:
    video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
    ret, frame = video.read()
    frames.append(frame)

#calculate the average
backgroundFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    
cv2.imwrite("bg.jpg",backgroundFrame)
