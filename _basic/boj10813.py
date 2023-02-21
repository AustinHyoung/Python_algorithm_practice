# 공 바꾸기

#n,m 입력
n, m = map(int, input().split())

arr = []

#리스트 초기화
for i in range(1, n+1):
  arr.append(i)

#서로 인덱스의 값 바꾸기
for x in range(m):
  i, j = map(int, input().split())
  temp = arr[i-1]
  arr[i-1] = arr[j-1]
  arr[j-1] = temp

#반복 출력
for i in range(n):
  print(arr[i], end=" ")