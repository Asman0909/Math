t = 0.2
eps = 0.00000001

# Вычисление e^t
e = 1
term = 1
k = 1

while abs(term) >= eps:
    term = term * t / k
    e += term
    k += 1

# Вычисление cos(t)
c = 1
term = 1
k = 1

while abs(term) >= eps:
    term = -term * t * t / ((2 * k - 1) * (2 * k))
    c += term
    k += 1

# Результат
F = e * c

print("e^t =", e)
print("cos(t) =", c)
print("F(t) =", F)