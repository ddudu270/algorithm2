from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()
        # 방문 안 한 모든 인접 노드를 큐에 넣기 위해 4방향 탐색
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] == 0 and graph[nx][ny]:  # 인접 노드 방문 안 했다면
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))  # 큐에 다 집어넣고
    return visit[N - 1][M - 1]


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]  # 대상 그래프
visit = [[0] * M for _ in range(N)]  # 방문 처리
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 왼 오 상 하

print(bfs(0, 0))
