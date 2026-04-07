# DFS 문제 + BFS 문제
# 각칸을 돌면서 왼, 오를 가고 4개 찍을때까지 가능한 모든 수 보면 됨
from collections import deque

def run_program():
    N, M = map(int, input().split())
    graph = []
    visited = [[False] * M for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_sum = 0

    def can_move(i, j):
        return 0 <= i < N and 0 <= j < M and not visited[i][j]
    
    def bfs(i, j):
        # 이거 굳이 bfs 아니고 일단 가능한거 다 더한다음 
        # 딱 3개다? -> sum이랑 max 비교
        # 4개다? 0 -> sum에서 가장 작은것 빼기
        # 이렇게 하면 훨씬 효율적
        def comb(count, now, sum_now):
            nonlocal max_sum
            if count == 3:
                if sum_now > max_sum:
                    max_sum = sum_now
            for k in range(now, 4):
                i_n = i + dx[k]
                j_n = j + dy[k]
                if can_move(i_n, j_n):
                    comb(count+1, k+1, sum_now + graph[i_n][j_n])
        comb(0, 0, graph[i][j])


    def dfs(i, j, sum_now, arr):
        nonlocal max_sum
        if len(arr) == 4:
            if sum_now > max_sum:
                max_sum = sum_now
            return
        for t in range(4):
            i_n = i + dx[t]
            j_n = j + dy[t]
            if can_move(i_n, j_n):
                val_now = graph[i_n][j_n]
                arr.append(val_now)
                visited[i_n][j_n] = True
                dfs(i_n, j_n, sum_now + val_now, arr)
                arr.pop()
                visited[i_n][j_n] = False

        

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            # DFS
            dfs(i, j, graph[i][j], [graph[i][j]])
            visited[i][j] = False
            # BFS
            bfs(i, j)

            
    print(max_sum)

run_program()