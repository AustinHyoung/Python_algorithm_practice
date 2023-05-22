def solution(s):
  c_cnt = 0
  z_cnt = 0
  answer = []
  res = s
  while len(res) > 1:
    z_cnt += res.count("0")
    res = res.replace("0", "")
    res_length = len(res)
    num = (bin(res_length))[2:]
    res = num
    c_cnt += 1

  answer.append(c_cnt)
  answer.append(z_cnt)

  return answer

print(solution("110010101001"))