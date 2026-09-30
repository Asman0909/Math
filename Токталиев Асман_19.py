x = 0.32
s = 1
term = 1
k = 0

while abs(term) >= 0.00000001:
    s += term
    k += 1
    term = -term * x * x / ((2 * k - 1) * (2 * k))

print("cos(0.32) =", s)
print("Количество членов:", k)