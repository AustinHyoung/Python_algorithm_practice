# 행렬 덧셈

n, m = map(int, input().split())

# A 행렬
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

# B 행렬
b = []
for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

# 결과
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j] + b[i][j])
    result.append(row)

# print(result)
# 출력
for row in result:
    for i in row:
        print(i, end=" ")
    print()



