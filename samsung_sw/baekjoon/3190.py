from collections import deque
def dir_change(curr_dir, change):
    left = {'E': 'N', 'W': 'S', 'N': 'W', 'S': 'E'}
    right = {'E': 'S', 'W': 'N', 'N': 'E', 'S': 'W'}
    if change == 'L':
        return left[curr_dir]
    else:
        return right[curr_dir]

def next_coor(i, j, dir):
    if dir == 'S':
        return [i+1, j]
    elif dir == 'N':
        return [i-1, j]
    elif dir == 'E':
        return [i, j+1]
    elif dir == 'W':
        return [i, j-1]

def run_program():

    N = int(input())
    K = int(input())
    command = {}
    # 0이면 비어있음, 1이면 뱀, 2이면 사과
    graph = [[0] * N for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        graph[i-1][j-1] = 2
    L = int(input())
    for _ in range(L):
        t, d = input().split()
        command[int(t)] = d

    # 뱀의 시작점
    graph[0][0] = 1
    time_now = 0
    snake_now = deque([[0, 0]])
    dir_now = 'E'
    def is_safe(i, j):
        return 0 <= i < N and 0 <= j < N and graph[i][j] != 1
    while True:
        # print(time_now, snake_now[0])
        # 머리의 다음 좌표 구하기
        head_now = snake_now[0]
        n_i, n_j = next_coor(head_now[0], head_now[1], dir_now)
        # print(n_i, n_j)
        # 시간 늘린다 (움직인다)
        time_now += 1
        # 좌표 벗어나거나 내 몸통과 부딪침
        if not is_safe(n_i, n_j):
            break
        # 빈칸임 -> 꼬리 하나 뗀다
        if graph[n_i][n_j] == 0:
            t_i, t_j = snake_now.pop()
            graph[t_i][t_j] = 0
        # 머리 옮긴다
        snake_now.appendleft([n_i, n_j])
        graph[n_i][n_j] = 1
        # 방향 전환 여부 check
        if time_now in command:
            change = command[time_now]
            dir_now = dir_change(dir_now, change)


    print(time_now)

run_program()

