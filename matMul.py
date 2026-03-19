from numpy import *
arr = array([[1,2,3,4],
            [5,6,7,8],
            [8,9,0,0]])
print(arr)
print(arr.dtype)
print(arr.shape)
arr2 = arr.flatten()

print(arr2)
print(arr2.shape)
arr3 = arr.reshape(2,2,3)
print(arr3)