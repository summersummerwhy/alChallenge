# 1. 비구름 이동명령대로 이동 (방향, 거리)
# 2. 이동한 곳에 물 증가
# 3. 구름 사라짐
# 4. 증가한 칸 check, 경계 안넘어가게
#    -> 물이 있는 바구니의 수만큼 물의 양 증가
# 5. 물의 양이 2 이상인 모든 칸에 구름이 생김, 물의 양 줄어듦
#    이때 3에서 구름 사라진 칸 아니어야함


def move(i, j, d, s, N):
    # 1, 2, 3, 4, 5, 6, 7, 8
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    dr = [None, 0, -1, -1, -1, 0, 1, 1, 1]
    dc = [None, -1, -1, 0, 1, 1, 1, 0, -1]
    n_i = (i + dr[d] * s) % N
    n_j = (j + dc[d] * s) % N
    return (n_i, n_j)

def run_program():
    N, M = map(int, input().split())
    graph = []
    commands = []
    cloud =[(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
    is_cloud = [[False] * N for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    for _ in range(M):
        commands.append(list(map(int, input().split())))

    def has_water(i, j):
        return 0 <= i < N and 0 <= j < N and graph[i][j] > 0

    dr = [1, 1, -1, -1]
    dc = [1, -1, 1, -1]

    for i in range(M):
        dir, sp = commands[i]
        for j in range(len(cloud)):
            n_i, n_j = move(cloud[j][0], cloud[j][1], dir, sp, N)
            # 비내리기
            graph[n_i][n_j] += 1
            is_cloud[n_i][n_j] = True
            cloud[j] = (n_i, n_j)
        magic = []
        amount = []
        for r, c in cloud:
            count = 0
            # 대각선 검사
            for t in range(4):
                r_n, c_n = r + dr[t], c + dc[t]
                if has_water(r_n, c_n):
                    count += 1
            if count > 0:
                magic.append((r, c))
                amount.append(count)
        for j in range(len(magic)):
            r, c = magic[j]
            graph[r][c] += amount[j]
        new_cloud = []
        for r in range(N):
            for c in range(N):
                if graph[r][c] >=2 and not is_cloud[r][c]:
                    graph[r][c] -= 2
                    new_cloud.append((r, c))
        for r, c in cloud:
            is_cloud[r][c] = False
        cloud = new_cloud
    ans = 0
    for i in range(N):
        ans += sum(graph[i])
    print(ans)


run_program()      

            

    

    

