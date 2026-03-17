import sys
from collections import deque

input = sys.stdin.readline

def count_group(N, group, graph, visited):
    xd = [1, -1, 0, 0]
    yd = [0, 0, 1, -1]
    group_num = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group_num += 1
                # BFS시작
                group_now = group[graph[i][j]]
                queue = deque()
                # 시작 원소
                queue.append([i, j])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for t in range(4):
                        now_x, now_y = x + xd[t], y + yd[t]
                        if (0 <= now_x <= N-1 and 0 <= now_y <= N-1 
                            and not visited[now_x][now_y] and group[graph[now_x][now_y]] == group_now):
                            # 이어지는 그룹이라고 판단
                            queue.append([now_x, now_y])
                            visited[now_x][now_y] = True
    return group_num

def make_visited(N):
    return [[False for _ in range(N)] for i in range(N)]

def run_program():
    N = int(input().strip())
    group = {'R': 1, 'G': 2, 'B': 3}
    graph = []
    for _ in range(N):
        graph.append(list(input()))
    # 적록색약 X
    print(count_group(N, group, graph, make_visited(N)), end = ' ')
    # 적룍색약 O
    group['G'] = 1
    print(count_group(N, group, graph, make_visited(N)))


run_program()

