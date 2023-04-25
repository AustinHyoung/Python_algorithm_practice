from itertools import permutations

n = int(input())

list = [i+1 for i in range(n)]

for i in permutations(list,n):

    for j in range(n):
        print(i[j],end = " ")
    print()