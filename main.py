import cv2
# 0 ref to main camera.
# If you want to use secondary came put 1
video = cv2.VideoCapture(0)

check, frame = video.read()

print(check)
print(frame)



