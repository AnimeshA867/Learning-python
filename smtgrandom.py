
str="Enter the number of desks in %s side:"

left=int(input(str % "left"))
right=int(input(str %"right"))

limit=left*3+right*3;
x= int(input("Enter today's attendance: "))

if(x>limit):
    print("Not enough space for %d students. "%(x))

elif x<=limit:
    print("Yea, the desks are enough for %d students." %x)


if(x%(left+right) == 0):
    print("Students are also equally distributed.")
else:
    print("Students are not equally distributed.")


print("  /\\")
print(" /  \\")
print("/____\\")