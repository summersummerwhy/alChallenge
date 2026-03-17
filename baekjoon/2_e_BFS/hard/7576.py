import sys
from collections import deque
# input 읽을때 
# 1, 0, -1 다 numbering

# 1. 0이 하나도 없으면 -> 바로 0 출력
# 2. 다 돌고나서 0 남아있으면 0 출력

input = sys.stdin.readline

def run_program():
    tomatoes = []
    M, N = map(int, input().strip().split())
    for _ in range(N):
        tomatoes.append(input().strip().split())
    riped, green, empty = 0, 0, 0
    for i in range(N):
        for j in range(M):
            tmt = tomatoes[i][j]
            if tmt == '1':
                riped += 1
            elif tmt == '0':
                green += 1
            else:
                empty == 0
    if green == 0:
        print(0)
        return
    days = [[-1 for _ in range(M)] for i in range(N)]
    visited = [[False for _ in range(M)] for i in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == '1':
                # BFS start
                queue.append([i, j])
                visited[i][j] = True
                days[i][j] = 0 
    # 1을 일단 추가한다음, queue를 돌리기 
    # why? zigzag로 1이 배치된 경우 오류가 날 수 있음
    while queue:
        x, y = queue.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for t in range(4):
            x_now, y_now = x + dx[t], y + dy[t]
            if (0 <= x_now <= N-1 and 0 <= y_now <= M-1
                and tomatoes[x_now][y_now] == '0'):
                # green -> riped
                if not visited[x_now][y_now]:
                    green -= 1
                    riped += 1
                    visited[x_now][y_now] = True
                    # days update
                    days[x_now][y_now] = days[x][y] + 1
                    # queue append
                    queue.append([x_now, y_now])
                else:
                    # 이미 방문해본적있다 -> 하지만 단축가능? queue에 넣기
                    if days[x][y] + 1 < days[x_now][y_now]:
                        days[x_now][y_now] = days[x][y] + 1
                        # queue append
                        queue.append([x_now, y_now])
    if green > 0:
        print(-1)
    else:
        day_max = -1
        for l in days:
            if max(l) > day_max:
                day_max = max(l)
        print(day_max)

run_program()