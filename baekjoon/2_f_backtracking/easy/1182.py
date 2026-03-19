import sys
from itertools import combinations


input = sys.stdin.readline

def run_program():
    N, S = map(int, input().strip().split())
    num = list(map(int, input().strip().split()))

    track = []
    ans = 0



    # def dfs(l, start):
    #     nonlocal ans
    #     if len(track) == l:
    #         if sum(track) == S:
    #             # print(track)
    #             ans += 1
    #         return
        
    #     for i in range(start, N):
    #         track.append(num[i])
    #         dfs(l, i+1)
    #         track.pop()
    
    for i in range(1, N+1):
        com_list = list(combinations(num, i))
        for com in com_list:
            if sum(com) == S:
                ans += 1

    print(ans)

run_program()


