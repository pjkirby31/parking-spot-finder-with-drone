import cv2

vidcap = cv2.VideoCapture('Drone footage/Videos/IMG_4535.MOV')
success,image = vidcap.read()
count = 0
while success:
  if count % 10==0:
    cv2.imwrite("Drone footage/Parking Spot Images/All/vertical/frame%d.png" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read frame: ', count)
  count += 1
