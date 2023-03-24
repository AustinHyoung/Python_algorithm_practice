# A -> B
# 그리디

from collections import deque

a, b = map(int, input().split())
queue = deque([(a, 1)])  # (현재 수, 연산 횟수)를 담은 튜플을 큐에 추가
visited = set([a])  # 이미 방문한 수를 저장하는 set

while queue:
    num, cnt = queue.popleft()

    if num == b:  # B에 도달한 경우, 연산 횟수 출력
        print(cnt)
        break

    # 2를 곱한 경우
    if num * 2 <= b and num * 2 not in visited:
        queue.append((num * 2, cnt + 1))
        visited.add(num * 2)

    # 1을 추가한 경우
    if num * 10 + 1 <= b and num * 10 + 1 not in visited:
        queue.append((num * 10 + 1, cnt + 1))
        visited.add(num * 10 + 1)

else:
    # B에 도달하지 못한 경우 -1 출력
    print(-1)