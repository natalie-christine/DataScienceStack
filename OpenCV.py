import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\JodaBook\Documents\Python\Python\DataScienceStack\bild.jpg")

img.shape
i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#plt.imshow(g, "grey")

#print(increased[0][0])
# plt.imshow(increased)
# plt.show()

#print(img.shape) --> (980, 1015, 3)

z = np.zeros((980, 1015, 3), dtype="uint8") + 80
increased = cv2.add(img, z)

# print(img[0][0])
# print(z[0][0])
# print(increased[0][0])

# plt.imshow(increased)
# plt.show()

newImg = cv2.rectangle(i,(300,500), (700,100), (0,0, 255), 10)
plt.imshow(newImg)
plt.show()

