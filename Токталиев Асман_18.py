import math

x = 12.31 - 4 * math.pi
s = 0
term = x
k = 0

while abs(term) >= 0.000001:
    s += term
    k += 1
    term = -term * x * x / ((2 * k) * (2 * k + 1))

print("sin(12.31) =", s)
print("Количество членов:", k)