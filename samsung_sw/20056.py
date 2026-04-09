# 일단 이동부터 구현


def move(i, j, N, dir, s):
    dr = [N-1, N-1, 0, 1, 1, 1, 0, N-1]
    dc = [0, 1, 1, 1, 0, N-1, N-1, N-1]
    dist = s % N
    while dist > 0:
        i = (i + dr[dir]) % N
        j = (j + dc[dir]) % N
        dist -= 1
    return i, j

# fireball: 구성품 [m, d, s]
# 한 칸마다 [[f], [f], ...]  이렇게 있음


def run_program():
    N, M, K = map(int, input().split())
    graph = [[[0, [], [], []] for _ in range(N)] for i in range(N)]
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        # fireball: 구성품 n, [m, d, s]
        graph[r-1][c-1][1].append(m)
        graph[r-1][c-1][2].append(d)
        graph[r-1][c-1][3].append(s)
        graph[r-1][c-1][0] += 1
    

    for time in range(K):
        new_graph = [[[0, [], [], []] for _ in range(N)] for i in range(N)]
        coor_set = set()
        # new_graph로 이동시키기
        for i in range(N):
            for j in range(N):
                fb_lst = graph[i][j]
                n = fb_lst[0]
                for t in range(n):
                    m, d, s = fb_lst[1][t], fb_lst[2][t], fb_lst[3][t]
                    n_i, n_j = move(i, j, N, d, s)
                    new_graph[n_i][n_j][1].append(m)
                    new_graph[n_i][n_j][2].append(d)
                    new_graph[n_i][n_j][3].append(s)
                    new_graph[n_i][n_j][0] += 1
                    coor_set.add((n_i, n_j))

        # 각 칸마다 접근, 합치고 나누기
        for i, j in coor_set:
            fb_lst = new_graph[i][j]
            num = fb_lst[0]
            if num > 1:
                m_n = sum(fb_lst[1]) // 5
                s_n = sum(fb_lst[3]) // num
                all_odd, all_even = True, True
                for d in fb_lst[2]:
                    if d % 2 == 0:
                        all_odd = False
                    else:
                        all_even = False
                # update
                if m_n == 0:
                    new_graph[i][j] = [0, [], [], []]
                else:
                    fb_lst[0] = 4
                    fb_lst[1] = [m_n]*4
                    if all_odd or all_even:
                        fb_lst[2] = [0, 2, 4, 6]
                    else:
                        fb_lst[2] = [1, 3, 5, 7]
                    fb_lst[3] = [s_n]*4
        # graph update
        graph = new_graph


    ans = 0

    for i in range(N):
        for j in range(N):
            ans += sum(graph[i][j][1])
    
    print(ans)

run_program()