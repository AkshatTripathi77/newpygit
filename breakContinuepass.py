ava = 10
x = int(input("Enter the number of candies a user wants    :"))
i = 0
while i<x:
    if i>ava:
        print("Sorry!Only",ava,"Are available")
        break
    print("Candy")
    i+=1
print("bye")