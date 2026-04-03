def count(lst):
    more = 0
    less = 0
    for i in range(len(lst)):
        if len(lst[i]) > 5:
            more += 1
        else:
            less += 1

    return more,less
lst = ["Akshat","Ananya","Asha","Arpita","Diti"]
more,less = (count(lst))
print("More",more,"Less",less)
