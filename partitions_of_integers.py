#   P(M, N) = {
#       1                       ,if M = 1
#       1                       ,if N = 1
#       P(M, M)                 ,if M < N
#       1 + P(M, M-1)           ,if M = N > 1
#       P(M, N-1) + P(M-N, N)   ,if M > N > 1
# }
import sys

parameter = [] * 2

print('P(M, N) is the number of different ways to express M as the sum of positive intergers not exceeding N')

for index in range(0, 2):
    if index == 0:
        position = 'M'
    else:
        position = 'N'
    if not parameter:
        print('Enter {0}\'s number in P(M, N)'.format(position))
    else:
        print('Enter {0}\'s number in P({1}, N)'.format(
            position, parameter[0]))

    inputNum = int(input())
    parameter.append(inputNum)


def P(M, N):
    if M == 1:
        return 1
    elif N == 1:
        return 1
    elif M < N:
        return P(M, M)
    elif M == N and M > 1:
        return 1+P(M, M-1)
    elif M > N and M > 1 and N > 1:
        return P(M, N-1) + P(M-N, N)


result = P(parameter[0], parameter[1])
print('=> P({0}, {1}) = {2}'.format(parameter[0], parameter[1], result))
print('Number of different partitions of {0} with positive intergers not exceeding {1} is {2}'.format(
    parameter[0], parameter[1], result))
