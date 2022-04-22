from numpy import number, random

# data = random.randint(20, size=(9))
# print('data = ', data)
data = [2, 5, 8, 6, 3, 9, 10, 15, 20]
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def Adjust(tree, index, numberOfelement):
    x = tree[index]
    j = (2 * index)+1
    while(j <= numberOfelement):
        # 有Rchild
        if(j < numberOfelement):
            # 取Max{ Lchild, Rchild }
            if tree[j] < tree[j+1]:
                j = j+1
        if(x >= tree[j]):
            break
        else:
            # Max{ Lchild, Rchild } > x, 故擺到x位置
            tree[int((j-1)/2)] = tree[j]
            j = (2 * j)+1
    # x >= 現在比較之node, 故放入其位置
    tree[int(j/2)] = x
    print(tree)


def Build(tree, numberOfelement):
    n = int((numberOfelement//2)-1)
    for index in range(n, -1, -1):
        Adjust(tree, index, numberOfelement-1)


Build(data, len(data))
