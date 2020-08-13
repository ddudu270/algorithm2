n, m = map(int, input().split())

d= [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = [] # 지도 입력받을 곳r
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1 # 이미 지금 있는 곳은 방문
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 방문 체크
        x= nx
        y = ny
        count +=1
        turn_time = 0 # 한 칸 나아가면 무조건 초기화
        continue # 그리고 다시 시작
    else:
        turn_time += 1 # 그냥 회전만!
    if turn_time == 4:
        nx = x -dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
            turn_time =0
        else:
            break

print(count)



