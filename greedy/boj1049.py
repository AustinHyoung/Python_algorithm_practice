# 기타줄
# 그리디

# 끊어진 줄이 6개 이상이면 => 패키지 제일 싼거 + 낱개로 제일 싼거
# 6개 이하이면 => 끊어진 줄 * 낱개 가격 제일 싼거 if 패키지가 더싸다? 그럼 패키지 가격으로

n, m = map(int, input().split())
lst = []

for i in range(m):
  row = list(map(int, input().split()))
  lst.append(row)

package = min([package_lst[0] for package_lst in lst])
single = min([single_lst[1] for single_lst in lst])

if package <= single * 6:  # 패키지가 더 저렴한 경우
  cnt = n // 6
  if n % 6 == 0:
    print(cnt * package)
  else:
    print(min(cnt * package + (n % 6) * single, (cnt + 1) * package))
else:  # 싱글 기타줄이 더 저렴한 경우
  print(min(single * n, package * ((n + 5) // 6)))