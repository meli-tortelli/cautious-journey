s = "algoritmos"
for c in s:
    if c in "aeiou":
        print("c:", c)

l = ["a", "b", "c"]
for i in range(len(l)):
    print("i:", l[i])

for x in range(10):
    print("x:", x)

for y in range(1, 20, 2):
    print("y:", y)

acc = 0
for z in range(1, 101):
    if z % 2 == 0:
        acc = acc + z
print("acc:", acc)

str_list = ["meli", "marti", "dmi"]
for name in str_list:
    for c in name:
        if c in "aeiou":
            print(c)
