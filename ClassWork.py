import cv2 as cv
'''import argparse
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect facesq
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (2,2,2),-1,2)
            frame = cv.line(frame, eye_center, eye_center, (0, 255, 0), 2)
    cv.imshow('Capture - Face detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera devide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
 
       break'''

'''import pytesseract as py
img = cv.imread("blood report.jpg",1)
# print(img)
text = py.image_to_string("blood report.jpg")
# print(text)
lis = text.split()
print(lis)'''
'''
from gtts import gTTS
tts = gTTS('तुम कैसे हो', lang='en')

tts.save('hello.mp3')
'''
'''from sklearn.datasets import load_iris
from sklearn import tree

irisdata = load_iris()
print(irisdata.data)
model = tree.DecisionTreeClassifier()
model.fit(irisdata.data, irisdata.target)
imput = [6.9, 3.1, 5.4, 2.1]
prediction = model.predict([imput])
print(prediction)
import graphviz as g
data = tree.export_graphviz(model,out_file=None)
graph = g.Source(data)
graph.render("new graph")
graph.view()'''
'''import cv2
img = cv2.imread('quote.jpg')
# get image height, width
(h, w) = img.shape[:2]
# calculate the center of the image
center = (w / 2, h / 2)

angle90 = 90
angle180 = 180
angle270 = 270

scale = 1.0

# Perform the counter clockwise rotation holding at the center
# 90 degrees
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

# 180 degrees
M = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M, (w, h))

# 270 degrees
M = cv2.getRotationMatrix2D(center, angle270, scale)
rotated270 = cv2.warpAffine(img, M, (h, w))

cv2.imshow('Original Image', img)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('Image rotated by 90 degrees', rotated90)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('Image rotated by 180 degrees', rotated180)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('Image rotated by 270 degrees', rotated270)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image'''
'''import math
import matplotlib.pyplot as plt
import numpy as np

lis = np.arange(-2,1,0.001)
linear = [i for i in lis]
lam = lambda x : 1 if x>0 else 0
bin = list(map(lam, lis))
sigmoid = [(1/(1+math.exp(-i))) for i in lis]
hyper = [math.tanh(i) for i in lis]
lam1 = lambda x : x if x>=0 else 0
rlu = list(map(lam1,lis))
softmax = (np.exp(lis))/sum(np.exp(lis))
plt.plot(lis,linear,label="linear")
plt.plot(lis,bin,label="binary")
plt.plot(lis,sigmoid,label="sigmoid")
plt.plot(lis,rlu,label="recified linear")
plt.plot(lis,hyper,label="hyper")
plt.plot(lis,softmax,label="softmax")
plt.legend()
plt.grid()
plt.show()'''

'''import numpy as np
input1 = np.array([0,0])
input2 = np.array([0,1])
input3 = np.array([1,0])
input4 = np.array([1,1])

weights = np.array([0.5,0.5])
theta = 1
def activation(s):
    if s>= theta:
        return 1
    else:
        return 0
def summation(x,w):
    s = np.dot(x,w)
    print("s == ",s)
    y = activation(s)
    print("y == :",y)
    return y
output1 = summation(input1, weights)
output2 = summation(input2, weights)
output3 = summation(input3, weights)
output4 = summation(input4,weights)
print(output1, output2, output3, output4)'''

'''import numpy as np
class Preception:
    theta = 1
    def __init__(self,input , weights):
        self.input = input
        self.weights = weights
    def activation(self,s):
        if s >= Preception.theta:
            return 1
        else:
            return 0
    def summation(self):
        s = np.dot(self.input,self.weights)
        y = self.activation(s)
        print(y)
input1 = np.array([1,1])
weights = np.array([0.5,0.5])
model = Preception(input1,weights)
model.summation()
'''
'''
import numpy as np

# To Create Input Arrays
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

# Weights for Inputs
weights = np.array([1, 1])

# Define Activation Function and Threshold
theta = 0
def activation(s):  # Binary Unit Step :)
    if s >= theta:
        return 1
    else:
        return 0

def summation(x, w, b):
    s = np.dot(x, w) + b
    y = activation(s)
    return y

# bias = -1.5 # AND
bias = -0.5 # OR
output = summation(input1, weights, bias)
print("For",input1,"|",output)
output = summation(input2, weights, bias)
print("For",input2,"|",output)
output = summation(input3, weights, bias)
print("For",input3,"|",output)
output = summation(input4, weights, bias)
print("For",input4,"|",output)
'''

'''import numpy as np

input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])
theta = 1
def activation(s):
    if s >= theta:
        return 1
    else:
        return 0
def activationNot(s):
    if s >= -0.5:
        return 1
    else:
        return 0

def summationAnd(x,w):
    s = np.dot(x,w)
    y = activation(s)
    return y
def summationNot(x,w):
    s = x * w
    y = activationNot(s)
    return y
weightAnd = np.array([0.5,0.5])
weightOr = np.array([1.1,1.1])
weightNot = -1
#for and
outputAND1 = summationAnd(input1, weightAnd)
outputAND2 = summationAnd(input2, weightAnd)
outputAND3 = summationAnd(input3, weightAnd)
outputAND4 = summationAnd(input4, weightAnd)
print(outputAND1, outputAND2, outputAND3, outputAND4)

#for or
outputOR1 = summationAnd(input1, weightOr)
outputOR2 = summationAnd(input2, weightOr)
outputOR3 = summationAnd(input3, weightOr)
outputOR4 = summationAnd(input4, weightOr)
print(outputOR1, outputOR2, outputOR3, outputOR4)

outputNOT1 = summationNot(outputAND1,weightNot)
outputNOT2 = summationNot(outputAND2,weightNot)
outputNOT3 = summationNot(outputAND3,weightNot)
outputNOT4 = summationNot(outputAND4,weightNot)
print(outputNOT1, outputNOT2, outputNOT3, outputNOT4)
newinput1 = np.array([outputOR1, outputNOT1])
newinput2 = np.array([outputOR2, outputNOT2])
newinput3 = np.array([outputOR3, outputNOT3])
newinput4 = np.array([outputOR4, outputNOT4])
FinalOutput1 = summationAnd(newinput1, weightAnd)
FinalOutput2 = summationAnd(newinput2, weightAnd)
FinalOutput3 = summationAnd(newinput3, weightAnd)
FinalOutput4 = summationAnd(newinput4, weightAnd)
print(FinalOutput1, FinalOutput2, FinalOutput3, FinalOutput4)'''
from sklearn.datasets import load_digits
import cv2 as cv
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
'''digits = load_digits()
print(digits["images"][0])'''
# cv.imshow("titsle",arr["images"][0])
# cv.waitKey(0)
# plt.subplot(2, 4, 1)
# plt.imshow(arr.images[0], cmap="Blues")
# plt.subplot(2, 4, 2)
# plt.imshow(arr.images[1], cmap="Blues")
# plt.show()
# plt.show()
'''X = digits.data
Y = digits.target

model = svm.SVC(gamma='scale')
model.fit(X, Y)

inputSample = digits.data[4]
print(digits.images[4])
print(digits.data[4])

predictedClass = model.predict([inputSample])

print(">> Predicted Class is:", predictedClass)'''
'''data = load_iris()
X = data.data
print(X)
model = KMeans(n_clusters=4)
model.fit(X)
predition  = model.predict(X)
print(predition)
# print(model)'''
# import torch
# import numpy as np
# X = torch.zeros(5,3,dtype=torch.int)
# # X = np.array(X)
# # X = X.numpy()
# print(X.size(), type(X))

import os
import numpy as np
import cv2 as cv
import csv
import torch
import tensorflow as tf
from tensorflow import keras
catTrain = os.listdir("C:/Users/Arsh/PycharmProjects/tictaktoe/training_set/cats")

dogTrain = os.listdir("C:/Users/Arsh/PycharmProjects/tictaktoe/training_set/dogs")
train_images = []
train_Labels = []
for i in range(len(dogTrain)):
    dogFile = "C:/Users/Arsh/PycharmProjects/tictaktoe/training_set/dogs/" + dogTrain[i]
    img = cv.imread(dogFile, 1)
    img = cv.resize(img, (120, 120))
#     # print(img.shape)
    with open("arsh1.csv", "a") as myfile:
        wr = csv.writer(myfile)
        wr.writerow(img)
    train_Labels.append(0)
    # train_images.append(img)

# for i in range(len(catTrain)):
#     catFile = "C:/Users/Arsh/PycharmProjects/tictaktoe/training_set/cats/" + catTrain[i]
#     img = cv.imread(catFile, 1)
#     img = cv.resize(img, (120, 120))
#     # print(img.shape)
#     train_Labels.append(1)
#
#     train_images.append(img)
# train_images = np.array(train_images)
# print(train_images.shape)

# img = cv.resize(img,(120,120))
# img = img.reshape(1,-1)
# cv.imshow("dog", img)
# cv.waitKey(0)
# print(img.shape)
# img = cv.resize(img, (120, 120))
# tenso = torch.Tensor(img)
# print(type(tenso))
# print(type(imgn))
# cv.imshow("dog", img)
#
