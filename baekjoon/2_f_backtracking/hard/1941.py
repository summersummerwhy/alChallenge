import sys
from collections import deque
from itertools import combinations


input = sys.stdin.readline
def run_program():
    students = []
    seats = []
    for _ in range(5):
        students.append(list(input().strip()))
    for i in range(5):
        for j in range(5):
            seats.append([i, j])

    # 1. S파가 대다수인가
    def is_s_major(track):
        lee_count = 0
        for i, j in track:
            if students[i][j] == 'S':
                lee_count += 1
        return lee_count >= 4
    

    # 2. 서로 연결되어 있는가
    def is_connected(track):
        # BFS 진행, 그리고 모두 방문했는지 판단
        queue = deque()
        visited = [False for _ in range(7)]
        queue.append(track[0])
        visited[0] = False
        # BFS 시작
        while queue:
            x, y = queue.popleft()
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):
                x_next = x + dx[i]
                y_next = y + dy[i]
                if not (0 <= x_next < 7 and 0 <= y_next < 7):
                    continue
                if [x_next, y_next] not in track:
                    continue
                idx = track.index([x_next, y_next])
                if not visited[idx]:
                    visited[idx] = True
                    queue.append([x_next, y_next]) 
        return sum(visited) == 7
    
    ans = 0
    
    for comb in combinations(seats, 7):
        if is_s_major(comb) and is_connected(comb):
            ans += 1
    
    print(ans)

run_program()





