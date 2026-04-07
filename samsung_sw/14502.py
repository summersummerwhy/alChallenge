# BFS
from collections import deque

def count_max(graph, N, M, room_count):
    visited = [[False] * M for _ in range(N)]
    def can_move(i, j):
        return 0 <= i < N and 0 <= j < M and graph[i][j] == 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2 and not visited[i][j]:
                queue = deque([[i, j]])
                visited[i][j] == True
                while queue:
                    x, y = queue.popleft()
                    for t in range(4):
                        x_next = x + dx[t]
                        y_next = y + dy[t]
                        if can_move(x_next, y_next):
                            queue.append([x_next, y_next])
                            visited[x_next][y_next] = True
                            graph[x_next][y_next] = 2
                            room_count -= 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return room_count


def run_program():
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    room_count = 0
    room_list = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                room_count += 1
                room_list.append([i, j])
    # 이제 세개 뽑아서 벽으로 만들기
    ans = 0
    def pick_three(now, count):
        nonlocal ans
        if count == 3:
            graph_copy = [g.copy() for g in graph]
            count_now = count_max(graph_copy, N, M, room_count -3)
            if count_now > ans:
                ans = count_now
            return
        for i in range(now, room_count):
            x, y = room_list[i][0], room_list[i][1]
            graph[x][y] = 1
            pick_three(i+1, count+1)
            graph[x][y] = 0
    pick_three(0, 0)
    print(ans)

run_program()
            
        
            



