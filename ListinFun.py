def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else :
            odd += 1
    return even,odd
lst = [2,13,98,34,65,18,55,33,87]
even,odd = count(lst)
print("Even = ",even, "odd = ",odd)