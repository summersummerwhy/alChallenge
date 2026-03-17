import sys
from collections import deque

input = sys.stdin.readline

def run_program():
    N, M = map(int, input().strip().split())
    graph = []
    visited = [[False for _ in range(M)] for i in range(N)]
    depth = [[0 for _ in range(M)] for i in range(N)]
    for _ in range(N):
        graph.append(list(input()))

    queue = deque()
    queue.append([0, 0])
    depth[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        # 좌우 이동하며 길 찾기
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            x_a = x + dx[i]
            y_a = y + dy[i]
            if (0 <= x_a <= N-1 and 0 <= y_a <= M-1 and graph[x_a][y_a] == '1' 
                and not visited[x_a][y_a]):
                queue.append([x_a, y_a])
                visited[x_a][y_a] = True
                depth[x_a][y_a] = depth[x][y] + 1
    
    print(depth[N-1][M-1])

run_program()

    
