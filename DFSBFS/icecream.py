def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < M and 0 <= nx < N:
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                dfs(nx, ny)


N, M = map(int, input().split())  # N이 행 M이 열의 개수
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for i in range(N)]  # 방문 처리
count = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]  # 왼 오 상 하

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)
