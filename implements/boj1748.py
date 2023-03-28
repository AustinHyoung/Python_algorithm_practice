# 수 이어 쓰기 1
# 구현
n = int(input())
result = 0
digit = len(str(n))  # n의 자리수

# 1~9, 10~99, 100~999, ... 에서의 숫자의 자리수 합을 미리 계산
for i in range(1, digit):
    result += i * (10**i - 10**(i-1))

# n이 속한 구간에서의 숫자의 자리수 합 계산
result += digit * (n - 10**(digit-1) + 1)

print(result)