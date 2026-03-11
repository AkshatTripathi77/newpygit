from array import *
arr = array('i',[])
n = int(input("Enter the length of an array   :"))
for i in range(n):
    x = int(input("Enter a value"))
    arr.append(x)
print(arr)
k=0
val = int(input("Enter a value"))
for e in arr:
    if e==val:
        print(k)
        break
    k+=1

