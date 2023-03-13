import math

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais.")
elif delta == 0:
    r = -b / (2 * a)
    print(f"a raiz desta equação é {r}.")
else:
    r_1 = (-b + math.sqrt(delta)) / (2 * a)
    r_2 = (-b - math.sqrt(delta)) / (2 * a)

    if r_1 < r_2:
        ordem = print(f" as raízes da equação são {r_1} e {r_2}")
    else:
        ordem = print(f"as raízes da equação são {r_2} e {r_1}")
