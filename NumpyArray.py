import matplotlib.pyplot as plt
import numpy as np

xs = np.arange(10)
ys = xs ** 2

plt.plot(xs, ys)
# plt.show()

newArray = np.array([1, 2, 3, 3, 4, 2, 1, 2, 4, 2])  # Umwandlung in ein NumPy-Array
mean = newArray.mean()
min = newArray.min()
max = newArray.max()
std = newArray.std()

# print(mean)
# print(min)
# print(max)
# print(std)

b = np.array([False, True, True, False, True, True, False, False, True, True])

trueValues = newArray[b] 
c = newArray >= 3
#print(newArray[c])

reshapeArray = newArray.reshape((2,5))
print(reshapeArray)
print("shape : " + str(reshapeArray.shape)) 

reshapeArray = newArray.reshape((5,-1))
print(reshapeArray)
print("shape : " + str(reshapeArray.shape)) 

reshapeArray = newArray.reshape(-1)
print(reshapeArray)
print("shape : " + str(reshapeArray.shape)) 