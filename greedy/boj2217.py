# 로프
# 그리디

n = int(input())
arr = sorted([int(input()) for _ in range(n)],reverse=True)
answer = 0
for i in range(n):
    answer = max(answer, arr[i]*(i+1))
print(answer)
