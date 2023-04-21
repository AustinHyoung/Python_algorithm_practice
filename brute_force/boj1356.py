# 어떤수 => 10진수 => 수를 두부분으로 나눔 => 앞부분 자리수 곱 == 뒷부분 자리수 곱

n = int(input())
str_n = str(n)
length = len(str_n)

def solve():
  answer = "NO"
  if length == 1:
    return answer
  
  for i in range(1, length):
    one = str_n[0:i]
    two = str_n[i:length]
    one_sum = 1
    two_sum = 1

    for j in one:
      one_sum *= int(j)

    for k in two:
      two_sum *= int(k)
    
    if one_sum == two_sum:
      answer = "YES"
      return answer
  return answer
    
print(solve())