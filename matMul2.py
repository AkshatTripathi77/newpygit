from numpy import *
m = matrix('123;456;789')
print(m)
print(diagonal(m))
print(m.min())
print(m.max())
print(m.sum())
m1 = matrix('1 2 3;4 2 6;7 9 8')
m2 = matrix('9 8 3;7 4 5;8 3 6')
m3 = m1 +m2
print(m3)
m4 = m1 * m2
print(m4)