# 거스름돈
# 그리디

money = int(input())
arr = [500, 100, 50, 10, 5, 1]

cnt = 0
change_money = 1000 - money

for i in arr:
  cnt += (change_money // i)
  change_money = (change_money % i)

print(cnt)