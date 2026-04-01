# 1. 신이 준 문자열 앞부터 자른거 모두 set에 보관
    # 1. 부분.... 2. 완성인거...
    # 부분이면서 완성이면? 그래도 킵고잉해야지
# 2. dfs로 매번 움직일때마다 네방향으로 이동
    # 완성이면 += 1
    # 부분 아니면 거기서 종료
    # 부분이면 계속

import sys

input = sys.stdin.readline

def run_program():
    N, M, K = map(int, input().strip().split())
    graph = []
    word_result = []
    word = {}
    subword = set()

    for _ in range(N):
        graph.append(list(input().strip()))
    
    for _ in range(K):
        w = input().strip()
        word[w] = 0
        word_result.append(w)
    
    for w in word:
        # 1개짜리 ~ # n-1개짜리
        # [:1] ~ [:n-1]
        n = len(w)
        for i in range(1, n):
            subword.add(w[:i])

    def get_next_idx(i, j, dir):
        nonlocal N, M
        if dir == 'u': 
            return (i - 1) % N, j
        elif dir == 'd':
            return (i + 1) % N, j
        elif dir == 'r':
            return i, (j + 1) % M
        elif dir == 'l':
            return i, (j - 1) % M
        elif dir == 'd1':
            return (i + 1) % N, (j + 1) % M
        elif dir == 'd2':
            return (i + 1) % N, (j - 1) % M
        elif dir == 'd3':
            return (i - 1) % N, (j + 1) % M
        elif dir == 'd4':
            return (i - 1) % N, (j - 1) % M

    def dfs(i, j, str_now):
        str_updated = str_now + graph[i][j]
        
        if str_updated in word:
            word[str_updated] += 1
            
        if str_updated in subword:
            for dir in ['u', 'd', 'r', 'l', 'd1', 'd2', 'd3', 'd4']:
                next_i, next_j = get_next_idx(i, j, dir)
                dfs(next_i, next_j, str_updated)

    for i in range(N):
        for j in range(M):
            dfs(i, j, "")
    
    for w in word_result:
        print(word[w])

run_program()



