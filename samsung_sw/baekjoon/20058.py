# 1 2  -> 3 1    new[y][N-1-x] = old[x][y]
# 3 4     4 2    
from collections import deque

def rotate_90(x, y, length, arr):
    new_arr = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            # 회전시킨거 length짜리 공간에 보관
            new_arr[j][length-1-i] = arr[x+i][y+j]

    for i in range(length):
        for j in range(length):
            arr[x+i][y+j] = new_arr[i][j]
        
    
def run_program():
    N, Q = map(int, input().split())
    M = 2**N
    L = []
    graph = []
    walls = [[4] * M for _ in range(M)]
    # 각 칸마다 붙어있는 네곳, 얼음 결과
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for _ in range(M):
        graph.append(list(map(int, input().split())))
    L = list(map(int, input().split()))
    for i in range(1, M-1):
        graph[i][0] 
            
            
    def has_ice(i, j):
        return 0 <= i < M and 0 <= j < M and graph[i][j] > 0
    for Li in L:
        # [0, 0] [0, 2**Li] ... [0, ]
        step = 2**Li
        # 격자 나누기
        if Li > 0:
            for i in range(0, M, step):
                for j in range(0, M, step):
                    # 격자별로 시계 방향 rotate
                    rotate_90(i, j, step, graph) 
        melted_coor = []
        for i in range(M):
            for j in range(M):
                ice_count = 0
                for t in range(4):
                    i_n, j_n = i + dx[t], j + dy[t]
                    if has_ice(i_n, j_n):
                        ice_count += 1
                if ice_count < 3 and graph[i][j] > 0:
                    melted_coor.append((i, j))
        for i, j in melted_coor:
            graph[i][j] -= 1
    ice_sum = 0
    ice_area_max = 0
    visited =  [[False] * M for _ in range(M)]
    # 다 끝나고 BFS로 덩어리 최대개수 쓰기
    for i in range(M):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                ice_area = 1
                ice_sum += graph[i][j]
                while queue:
                    x, y = queue.popleft()
                    for t in range(4):
                        x_n, y_n = x + dx[t], y + dy[t]
                        if has_ice(x_n, y_n) and not visited[x_n][y_n]:
                            queue.append((x_n, y_n))
                            visited[x_n][y_n] = True
                            ice_area += 1
                            ice_sum += graph[x_n][y_n]
                ice_area_max = max(ice_area_max, ice_area)
    print(ice_sum)
    print(ice_area_max)

                

run_program()
            





