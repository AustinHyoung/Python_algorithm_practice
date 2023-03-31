# 한조서열정리하고옴
# 그리디

N = int(input())

mountines = list(map(int, input().split()))
cnt = 0
maxMountine = 0
result = []

for mountine in mountines: 
    if mountine > maxMountine: # 사람들의 높이를 비교함 (만약 i번째 값이 가장 높은 값보다 높은 경우)
        maxMountine = mountine # 가장 높은 봉우리의 값이 변경
        cnt = 0 # 그로인해 잡은 수는 초기화
    else:
        cnt += 1 # 봉우리가 가장 높기 때문에 계속해서 잡은 수를 증가시킴
    result.append(cnt) # 높이 비교해서 초기화 될때마다 리스트에 잡은 수를 추가 시킴

print(result) # 리스트에서 가장 높은 수를 찾으면 답

