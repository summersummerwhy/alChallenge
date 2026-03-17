import sys
import math 
from collections import deque
    
input = sys.stdin.readline

def run_program():
    R, C = map(int, input().strip().split())
    graph = []
    for _ in range(R):
        graph.append(list(input()))
    f_time = [[math.inf for _ in range(C)] for i in range(R)]
    j_time = [[math.inf for _ in range(C)] for i in range(R)]
    f_queue = deque()
    j_queue = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'F':
                f_time[i][j] = 0
                f_queue.append([i, j])
            elif graph[i][j] == 'J':
                j_time[i][j] = 0
                j_queue.append([i, j])
    # <불> 부터 BFS 시작
    # 불이 지나가는 <가장 빠른> 시간을 기록해둔다
    xd = [1, -1, 0, 0]
    yd = [0, 0, 1, -1]
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            x_now = x + xd[i]
            y_now = y + yd[i]
            if (0 <= x_now <= R-1 and 0 <= y_now <= C-1 and
                graph[x_now][y_now] != '#'):
                if f_time[x][y] + 1 < f_time[x_now][y_now]:
                    f_time[x_now][y_now] = f_time[x][y] + 1
                    f_queue.append([x_now, y_now])
    # 이제 지훈이의 차례
    # 1. 이전의 자신보다 빨리 
    # 2. 그리고 "불보다 빨리"인 경우 update를 한다           
    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            x_now = x + xd[i]
            y_now = y + yd[i]
            if (0 <= x_now <= R-1 and 0 <= y_now <= C-1 and
                graph[x_now][y_now] != '#'):
                if (j_time[x][y] + 1 < j_time[x_now][y_now] and 
                    j_time[x][y] + 1 < f_time[x_now][y_now]):
                    j_time[x_now][y_now] = j_time[x][y] + 1
                    j_queue.append([x_now, y_now])
    # 가장자리를 훑으며 최소시간 여부 update
    min_time = math.inf
    # 왼, 오
    for i in range(R):
        min_time = min([min_time, j_time[i][0], j_time[i][C-1]])
    # 위, 아래
    for j in range(1, C-1):
        min_time = min([min_time, j_time[0][j], j_time[R-1][j]])
    if min_time == math.inf:
        print("IMPOSSIBLE")
    else:
        print(min_time + 1)
    
        
run_program()