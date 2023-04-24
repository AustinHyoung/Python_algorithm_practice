# 인덱스값+1 + 일수  > n 이면 불필요
# 첫 인덱스부터 계산

n = int(input())
work_day = [list(map(int, input().split())) for _ in range(n)]

answer = 0
def solve(day, payment):
  global answer
  answer = max(answer, payment)

  if day >= n:
    return

  if day + work_day[day][0] <= n:
    solve(day + work_day[day][0], payment + work_day[day][1])
    solve(day+1, payment)
  else:
    solve(day+1, payment)
  return

solve(0,0)

print(answer)