# 1. R: 안막혀있는 방향 + 아직 안방문한 방향 찾아보기
# 2. 움직인다
# 벽이 나올때까지 방향으로 가다가 구멍 나오면 break
# 벽 바로 앞에 멈추기...
# 3. R, B 같이 있으면? 
# 방향에 따라 
# 왼, 오면 R,B 같은 row인지 check
# 위, 아래면 R,B 같은 column인지 check
# 더 가까운것부터 움직이기

def move_sp(R, B, graph, dir):
    # 0: r, 1: l, 2: u, 3: d 
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    R_done = False
    B_done = False
    sp_lst = ['R', 'B']
    # 일단 R, B중 어떤 순서로 update할지 고르기
    if R[0] == B[0]: # 같은 row
        if dir == 0 and B[1] > R[1]:
            sp_lst = ['B', 'R']
        elif dir == 1 and B[1] < R[1]:
            sp_lst = ['B', 'R']
    elif R[1] == B[1]: # 같은 col
        if dir == 2 and B[0] < R[0]:
            sp_lst = ['B', 'R']
        elif dir == 3 and B[0] > R[0]:
            sp_lst = ['B', 'R']
    for sp in sp_lst:
        x_now, y_now = -1, -1
        if sp == 'R':
            x_now, y_now = R[0], R[1]
        else:
            x_now, y_now = B[0], B[1]
        graph[x_now][y_now] = '.'
        while True:

            x_next = x_now + dx[dir]
            y_next = y_now + dy[dir]
            # 1. 벽/구멍/구슬이면 멈추기
            # 2. 그냥 빈칸이면 계속 이동
            if graph[x_next][y_next] != '.':
                graph[x_now][y_now] = sp
                break
            x_now = x_next
            y_now = y_next


        if sp == 'R':
            R = [x_now, y_now]
            if graph[x_next][y_next] == 'O':
                R_done = True
        else:
            B = [x_now, y_now]
            if graph[x_next][y_next] == 'O':
                B_done = True
            if R_done and graph[x_next][y_next] == 'R':
                R_done = False
                B_done = True

    return R, B, R_done, B_done 

min_num = 11

def dfs(R, B, graph, N, M, num, dir_bf=-1):
    global min_num
    if num > 10:
        return
    # 비어있고 움직일 방향 찾아내기
    # 0: r, 1: l, 2: u, 3: d 
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # 다시 왔던 곳으로 움직이면 안됨
    opp_dir = {0: 1, 1: 0, 2: 3, 3: 2}
    def is_empty(x, y):
        return 0<= x < N and 0 <= y < M and (graph[x][y] == '.' or graph[x][y] == 'O')
    next_dir = []
    for d in range(4):
        x_n = R[0] + dx[d]
        y_n = R[1] + dy[d]
        x_n_b = B[0] + dx[d]
        y_n_b = B[1] + dy[d]
        if (dir_bf == -1 or d != opp_dir[dir_bf]):
            if is_empty(x_n, y_n) and (dir_bf == -1 or d != opp_dir[dir_bf]):
                next_dir.append(d)
            elif is_empty(x_n_b, y_n_b):
                next_dir.append(d)
    # 해당 방향으로 움직여서 update된 graph 찾아내기
    # 근데? 그 와중에 R, B 구멍에 떨어졌는지 여부도 알아야됨
    # print(next_dir)
    for dir in next_dir:
        graph_copy = [i.copy() for i in graph]
        R_n, B_n, R_done, B_done = move_sp(R, B, graph_copy, dir)
        # print(f"dir: {dir}")
        # print(R_n, B_n, R_done, B_done)
        if R_done:
            min_num = min(num, min_num)
            continue
        elif B_done:
            continue
        dfs(R_n, B_n, graph_copy, N, M, num + 1, dir)



N, M = map(int, input().split())
graph = []
R = [-1, -1]
B = [-1, -1]
for _ in range(N):
    graph.append(list(input()))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            R = [i, j]
        elif graph[i][j] == 'B':
            B = [i, j]

dfs(R, B, graph, N, M, 1)
if min_num == 11:
    print(-1)
else:
    print(min_num)