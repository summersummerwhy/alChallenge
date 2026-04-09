
def get_dict(y, i, j, dir):
    # 서 남 동 북
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    tor_d = {}
    sand_left = y
    # x: graph[i][j]
    # y: graph[n_i][n_j] -> 얘만 신경쓰면 됨
    # 1. 7%
    tor_d[(i+di[(dir+1)%4], j+dj[(dir+1)%4])] = int(0.07*y)
    tor_d[(i+di[(dir-1)%4], j+dj[(dir-1)%4])]= int(0.07*y)
    sand_left -= 2  * int(0.07*y)
    # 2. 10%
    tor_d[(i+di[dir]+di[(dir+1)%4], j+dj[dir]+dj[(dir+1)%4])] = int(0.1*y)
    tor_d[(i+di[dir]+di[(dir-1)%4], j+dj[dir]+dj[(dir-1)%4])] = int(0.1*y)
    sand_left -= 2  * int(0.1*y)
    # 3. 1%
    tor_d[(i-di[dir]+di[(dir+1)%4], j-dj[dir]+dj[(dir+1)%4])] = int(0.01*y)
    tor_d[(i-di[dir]+di[(dir-1)%4], j-dj[dir]+dj[(dir-1)%4])] = int(0.01*y)    
    sand_left -= 2  * int(0.01*y)
    # 4. 2%
    tor_d[(i+2*di[(dir+1)%4], j+2*dj[(dir+1)%4])] = int(0.02*y)
    tor_d[(i+2*di[(dir-1)%4], j+2*dj[(dir-1)%4])] = int(0.02*y)
    sand_left -= 2  * int(0.02*y)
    # 5. 5%
    tor_d[(i+2*di[dir], j+2*dj[dir])] = int(0.05*y)
    sand_left -= int(0.05*y)
    # 6. 나머지 
    tor_d[(i+di[dir], j+dj[dir])]= sand_left
    return tor_d



    

def move_tornado(N, graph):
    i, j = N//2, N//2
    dist = 1
    time = 0
    def inside(a, b):
        return 0 <= a < N and 0 <= b < N
    # 서 남 동 북
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    dir = 0
    sand_out = 0
    while True:
        for _ in range(dist):
            # 이동
            n_i = i + di[dir]
            n_j = j + dj[dir]
            # 이동 후 범위 벗어났으면 종료
            if not inside(n_i, n_j):
                return sand_out
            sand_now = graph[n_i][n_j]
            d = get_dict(sand_now, n_i, n_j, dir)
            graph[n_i][n_j] = 0
            for key, value in d.items():
                x, y = key
                if inside(x, y):
                    graph[x][y] += value
                else:
                    sand_out += value
            i = n_i
            j = n_j
        dir = (dir + 1) % 4
        time += 1
        if time == 2:
            time = 0
            dist += 1

def run_program():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    print(move_tornado(N, graph))

run_program()
