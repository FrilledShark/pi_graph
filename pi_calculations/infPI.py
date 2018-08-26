from time import sleep
from decimal import Decimal, getcontext


getcontext().prec = 128

pi = 3

for i in range(1000000000000000):
    x = Decimal(i + 1)
    xa = x * 2
    xb = xa + 1
    xc = xa + 2
    if i % 2 == 0:
        pi += 4/(xa*xb*xc)
    else:
        pi -= 4 / (xa * xb * xc)
    if i % 50000 == 0:
        print(pi)

# picorrect = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)