import sys

input = sys.stdin.readline

def run_program():
    N, M = map(int, input().strip().split())
    num = list(map(int, input().strip().split()))
    num.sort()
    path = []
    # dfs 시작
    def dfs():
        if len(path) == M:
            print(' '.join(map(str, path)))
            return 
        
        for i in range(0, N):
            path.append(num[i])
            dfs()
            path.pop()
    
    dfs()

run_program()

