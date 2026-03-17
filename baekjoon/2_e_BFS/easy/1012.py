import sys
from collections import deque

input = sys.stdin.readline

# BFS:
# 1. queue에 시작 node 추가
# 2. 그 node와 인접한 node queue에 추가
# 3. 

def run_program():
    T = int(input().strip())
    for _ in range(T):
        M, N, K = map(int, input().strip().split())
        graph = [[0 for _ in range(N)] for i in range(M)]
        visited = [[False for _ in range(N)] for i in range(M)]
        queue = deque()
        for i in range(K):
            x, y = map(int, input().strip().split())
            graph[x][y] = 1
        # 좌우 이동용 좌표
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        # 최종 덩어리 수
        chunk_num = 0
        # 좌표 차례로 방문
        for i in range(M):
            for j in range(N):
                if graph[i][j] == 1 and not visited[i][j]:
                    # chunk 하나 추가
                    chunk_num += 1
                    # BFS 시작
                    queue.append([i, j])
                    visited[i][j] = True
                    while queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            next_x, next_y = x + dx[k], y + dy[k]
                            if 0 <= next_x <= M-1 and 0 <= next_y <= N-1 and \
                                graph[next_x][next_y] == 1 \
                                and not visited[next_x][next_y]:
                                queue.append([next_x, next_y])
                                visited[next_x][next_y] = True
        # 최종 정답 도출 
        print(chunk_num)

run_program()        


