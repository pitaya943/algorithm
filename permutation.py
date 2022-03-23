def swap(first, second):
    temp = target[first]
    target[first] = target[second]
    target[second] = temp


count = 0


def perm(list, start, end):
    global count
    if(start == end):
        count += 1
        print(list)

    else:
        for x in range(start, end + 1):
            swap(start, x)
            perm(list, start + 1, end)
            swap(start, x)


target = ['a', 'b', 'c', 'd', 'e']
perm(target, 0, len(target)-1)
print('There are %s permutations' % count)


def perms(word):
    stack = list(word)
    results = [stack.pop()]
    print(results)
    while len(stack) != 0:
        c = stack.pop()
        print(c)
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
                print(w[:i] + c + w[i:])

        results = new_results
    return results


print(perms('1234'))
