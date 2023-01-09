import numpy as np

a = np.array([[10,40],[30,20]])

print("Original array:")
print(a)

print("Sort the array along the first axis:")
print(np.sort(a, axis=0))

print("Sort the array along the last axis:")
print(np.sort(a))

print("Sort the flattened array:")
print(np.sort(a, axis=None))

#Below is the Output :

Original array:
[[10 40]
 [30 20]]
Sort the array along the first axis:
[[10 20]
 [30 40]]
Sort the array along the last axis:
[[10 40]
 [20 30]]
Sort the flattened array:
[10 20 30 40]
