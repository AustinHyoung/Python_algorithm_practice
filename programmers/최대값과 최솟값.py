def solution(s):
  lst = [int(x) for x in s.split()]
  min_val = min(lst)
  max_val = max(lst)
  answer = str(min_val) + ' ' + str(max_val)

  return answer

print(solution("1 2 3 4"))