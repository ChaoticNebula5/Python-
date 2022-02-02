import cv2
import numpy as np

config_file = "ObjectDetection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "ObjectDetection/frozen_inference_graph.pb"
model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
file_name = "ObjectDetection/Labels.txt"
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')


model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)  

img = cv2.imread("ObjectDetection/test.jpeg")

ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)



#img = "image.jpeg"

font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN


#ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.55)
for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
    cv2.rectangle(img, boxes,(255,0,0), 2 )        
    cv2.putText(img, classLabels[ClassInd-1], (boxes[0]+10,boxes[1]+40), font, fontScale=font_scale,color = (0,255,0), thickness=3)
    
cv2.imshow("Detected Objects", img)
cv2.waitKey(0)
cv2.DestroyAllWindows()