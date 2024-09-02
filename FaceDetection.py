import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\JodaBook\Documents\Python\Python\DataScienceStack\foto.jpeg")

#print(img.shape)
i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grey = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)

classifier = cv2.CascadeClassifier(r'C:\Users\JodaBook\Documents\Python\Kursmaterialien\data\haarcascades\haarcascade_frontalface_default.xml')

faces = classifier.detectMultiScale(grey, minNeighbors=4)
print(faces)

c = img.copy()
for face in faces:
    x, y, w, h = face
    cv2.rectangle(c, (x,y), (x + w, y+ h), (0, 255,0),5)
    print(face)
    
i = cv2.cvtColor(c, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()




