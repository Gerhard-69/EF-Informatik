def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

count = 10
number = factorial(count)
print(number)

zahl = 1
m= 10
for i in range(m-1):
    zahl = zahl * m
    m = m-1
print(zahl)