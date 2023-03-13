import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

distance = math.sqrt(((a - c) ** 2) + ((b - d) ** 2))

if distance >= 10:
    print("longe")
else:
    print("perto")
