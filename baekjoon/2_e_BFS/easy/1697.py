import sys
from collections import deque

input = sys.stdin.readline

def run_program():
    N, K = map(int, input().strip().split())

    visited = [False for _ in range(100001)]
    time = {}

    # 이것도 BFS
    # 걷기(x+1, x-1)와 순간이동(2x)을 "두 종류"의 이웃으로 취급하면 됨
    queue = deque()
    queue.append(N)
    visited[N] = True
    time[N] = 0
    while queue:
        x_now = queue.popleft()
        if x_now == K:
            print(time[x_now])
            break
        x_next = [x_now + 1, x_now -1, 2*x_now]
        for x in x_next:
            if 0 <= x <= 100000 and not visited[x]:
                queue.append(x)
                visited[x] = True
                time[x] = time[x_now] + 1

run_program()
