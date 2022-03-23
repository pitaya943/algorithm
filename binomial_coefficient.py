# (n m) = {
#   1                   ,if(n = m or m = 0)
#   (n-1 m) + (n-1 m-1) ,otherwise
# }

targetN = 5
targetM = 3
count = 0


def Bin(n, m):
    global count
    count += 1
    if (n == m or m == 0):
        return 1
    else:
        return (Bin(n - 1, m)+Bin(n - 1, m - 1))


print('Bin(%s, %s) = %s' % (targetN, targetM, Bin(targetN, targetM)))
print('Function ran %s times' % count)
