import cv2
 
img = cv2.imread('Parking Spot Images\\frame26860.png')
 
with open('training/obj.names', 'r') as f:
    classes = f.read().splitlines()

net = cv2.dnn.readNetFromDarknet('yolov4-tiny-custom.cfg', 'yolov4-tiny-custom_best.weights')

model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(640, 640), swapRB=True)

classIds, scores, boxes = model.detect(img, confThreshold=0.4, nmsThreshold=0.5)

for (classId, score, box) in zip(classIds, scores, boxes):
    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(0, 255, 0), thickness=2)
 
    text = '%s: %.2f' % (classes[classId[0]], score)
    cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=(0, 255, 0), thickness=2)
 
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()