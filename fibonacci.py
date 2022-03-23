# F(n) = {
#   0               ,if (n = 0)
#   1               ,if (n = 1)
#   F(n-1) + F(n-2) ,if (n >= 2)
# }

target = 10
count = 0


def Fibonacci(n):
    global count
    count += 1
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))


print('Fib(%s) = %s' % (target, Fibonacci(target)))
print('Function ran %s times' % count)


def Fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
    return c


print('Iterative - Fib(%s) = %s' % (target, Fib(target)))
