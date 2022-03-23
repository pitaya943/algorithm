# GCD(m, n) = {
#   n               ,if (m % n == 0)
#   GCD(n, m % n)   ,otherwise
# }

targetM = 2789
targetN = 7
count = 0


def GCD(m, n):
    global count
    count += 1
    if ((m % n) == 0):
        return n
    else:
        return GCD(n, (m % n))


print('GCD(%s, %s) = %s' % (targetM, targetN, GCD(targetM, targetN)))
print('Function ran %s times' % count)
