#개수 세기
import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(data.count(v))