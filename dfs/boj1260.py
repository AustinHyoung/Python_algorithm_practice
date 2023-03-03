from collections import deque

# DFS 함수 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V를 입력받음
N, M, V = map(int, input().split())

# 그래프 정보를 저장할 리스트 생성
graph = [[] for _ in range(N+1)]

# 간선 정보를 입력받아 그래프 생성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프의 각 정점이 방문되었는지 확인하기 위한 리스트 생성
visited = [False] * (N+1)

# 그래프의 각 정점에 연결된 인접 정점 리스트를 정렬
for i in range(1, N+1):
    graph[i].sort()

# DFS 수행 결과 출력
dfs(graph, V, visited)
print()

# BFS 수행 결과 출력
visited = [False] * (N+1)
bfs(graph, V, visited)

