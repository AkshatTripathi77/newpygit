a = 10
print(id(a))
def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("in Fun",a)
    globals()['a'] = 15
something()
print("out fun " ,a)
