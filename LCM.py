import random

def gcd(c, m):
    while m!= 0:
        c, m = m, c % m
    return c

def coprime(c, m):
    if gcd(c, m) == 1:
        return True

def factor(m):
    i = 2
    prim = []
    while i * i <= m:
        while m % i == 0:
            prim.append(i)
            m = m / i
        i = i + 1
    if m > 1:
        prim.append(n)
    return prim

def multiplicity1(a, prim):
    b = a - 1
    for i in prim:
        if b % prim[i] == 0:
            return True
        else:
            return False

def multiplicity2(a, m):
    b = a - 1
    if m % 4 == 0:
        if b % 4 == 0:
            return True
        return False
    return True

def generation():
    m = 65536
    prim = factor(m)
    x = random.randint(0, m - 1)
    while True:
        c = random.randint(0, m - 1)
        if coprime(c, m) == True:
            break
    while True:
        a = random.randint(0, m - 1)
        if multiplicity1(a, prim) == True and multiplicity2(a, m) == True:
            break
    return a, x, c, m

def LCG(a, x, c, m):
    x = (a * x + c) % m
    return x
    
n = int(input("iteration - "))
a = generation()[0]
x = generation()[1]
c = generation()[2]
m = generation()[3]
for i in range(n):
    x = LCG(a, x, c, m)
    print(x)