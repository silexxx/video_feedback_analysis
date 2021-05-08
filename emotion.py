import cv2
from progress.bar import Bar
from deepface import DeepFace

cap=cv2.VideoCapture('input_video/2.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
bar = Bar('Processing Frames', max=length)
for i in range(0, length):
    ret, frame = cap.read()
    cv2.imwrite("frame/1.jpg",frame)
    cv2.imshow("frame",frame)
    cv2.waitKey(1)
    # obj = DeepFace.analyze(img_path = "frame/1.jpg", actions = ['age', 'gender', 'race', 'emotion'],enforce_detection=False)
    # print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])
    bar.next()
bar.finish()