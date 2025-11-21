#funcionX

n = int(input("Ingresa el valor de n: "))

x = 0

print("x\tf(x)")

while x <= n:
    fx = x**3 + x**2 - 5
    print(f"{x}\t{fx}")
    x += 2  
