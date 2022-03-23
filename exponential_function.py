# RSA - Calculattion of C value
M = 1234
e = 17
MExponent = 1  # M^e
C = 1

p = 61
q = 127
n = p * q  # n = pq


def Exponential(base, exponent):
    global MExponent
    for i in range(0, exponent):
        MExponent = MExponent * base


def Module(MExponent, n):
    global C
    C = MExponent % n
    print("C's value is :", C)


Exponential(M, e)
Module(MExponent, n)

print("C = M^e mod pq")
print(C, "=", M, "^", e, "mod", n)
