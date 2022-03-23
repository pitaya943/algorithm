# A(m, n) = {
#   n + 1               ,if (m == 0)
#   A(m-1, 1)           ,if (n == 0)
#   A(m-1, A(m, n-1))   ,otherwise
# }

targetM = 3
targetN = 1
count = 0


def Ack(m, n):
    global count
    count += 1
    if (m == 0):
        return (n + 1)
    elif (n == 0):
        return Ack(m - 1, 1)
    else:
        return (Ack(m - 1, Ack(m, n - 1)))


print('Ack(%s, %s) = %s' % (targetM, targetN, Ack(targetM, targetN)))
print('Function ran %s times' % count)
