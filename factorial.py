# n! = {
#   1           ,if (n = 0)
#   n* (n-1)!   ,if (n >= 1)
# }

target = 3  # Target
count = 0   # Counter


def Factorial(n):

    global count
    count += 1

    if (n == 0):
        return 1
    else:
        return n * Factorial(n-1)


print('%s! = %s' % (target, Factorial(target)))
print('Function ran %s times' % count)
