from collections import deque
# 총 8개의 노드라고 가정하면 1부터 시작하기때문에 인덱스 개념의 0은 리스트를 비워둔다
graph = [[],[2, 3, 8],[1, 7],[1, 4, 5],[3, 5],[3, 4],[7],[2, 6, 8],[1, 7]]

# 각 노드가 방문된 정보를 true, false로 표현
visited = [False] * 9

def bfs(graph, start, visited):
  queue = deque([start])
  # 현재 노드 방문처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소 뽑아서 출력
    v = queue.popleft()
    print(v, end= ' ')
    # 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

bfs(graph, 1, visited)