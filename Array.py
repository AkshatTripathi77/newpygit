from array import *
vals = array('i',[5,9,8,4,2])
print(vals.buffer_info())
print(vals.typecode)
#vals.reverse()
#print(vals)
newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)
