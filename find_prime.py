from ntpath import join
from re import I
from time import process_time

bar_char = ['幹', '你', '娘'] * 20
# dick = ['二'] * 20

# A = 1
# B = 1
# C = 1
# D = 1


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    # global A, B, C, D
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)

    # if filledLength == 0 and A:
    #     dick.insert(0, '8')
    #     A = 0
    # elif filledLength == 22 and B:
    #     dick.append('D')
    #     B = 0
    # elif filledLength == 23 and C:
    #     dick.append('-')
    #     C = 0
    # elif filledLength == 24 and D:
    #     dick.append('3')
    #     D = 0

    # bar = ''.join(dick[0:int(filledLength/2)]) + \
    #     '-' * (length - filledLength)
    bar = ''.join(bar_char[0:int(filledLength/2)]) + \
        '-' * (length - filledLength)
    # bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)


targetNumber = int(
    input('Enter the number of defferent primes you want to find: '))

# specificIndex = int(
#     input('Enter the specific number of prime you want to find: '))

primes = [] * targetNumber


def AutoLoop():

    initialValue = 2

    while len(primes) <= targetNumber:
        if SingleNum(initialValue):
            primes.append(initialValue)
        initialValue += 1
        printProgressBar(len(primes), targetNumber, prefix='Progress:',
                         suffix='Complete', length=50)


def FindSpecificPrime(index):
    initialValue = 2
    while len(primes) < index:
        if SingleNum(initialValue):
            primes.append(initialValue)
        initialValue += 1
    return primes[index-1]


def SingleNum(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# main
start = process_time()
AutoLoop()
end = process_time()
# result = FindSpecificPrime(specificIndex)
print(
    '\n-------Top {0} Prime-------\n {1}\n-------Top {0} Prime-------'.format(targetNumber, primes))
# print('No.{0} prime is: {1}'.format(
#     specificIndex, result))
print(
    'Elapsed time during the whole program in seconds: {0}'.format(end-start))
