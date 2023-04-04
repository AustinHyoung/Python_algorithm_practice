# 컵홀더
# 그리디

n = int(input())
seats = input()

cupholders = seats.count("LL")

if cupholders <= 1:
  print(n)
else:
  print(n - cupholders + 1)

