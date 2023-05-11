def fibo(n):
  cnt_zero = [0] * 41
  cnt_one = [0] * 41

  cnt_zero[0] = 1
  cnt_one[1] = 1

  for i in range(2, n+1):
    cnt_zero[i] = cnt_zero[i-1] + cnt_zero[i-2]
    cnt_one[i] = cnt_one[i-1] + cnt_one[i-2]

  return cnt_zero[n], cnt_one[n]

T = int(input())

for _ in range(T):
  n = int(input())

  answer = fibo(n)
  print(answer[0], answer[1])