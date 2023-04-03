# 5와 6의 차이
# 그리디

a, b = map(int,input().split())

min_a = int(str(a).replace('6','5'))
min_b = int(str(b).replace('6','5'))

max_a = int(str(a).replace('5','6'))
max_b = int(str(b).replace('5','6'))

print(min_a + min_b, max_a + max_b)
