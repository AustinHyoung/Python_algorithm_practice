# 숫자의 합
import sys

a = int(input())
b = input()

if len(b) != a:
    print("err: a의 길이만큼 b를 입력해주세요")
    sys.exit(1)

sum = 0

for i in b:
    sum += int(i)

print(sum)


