# 퇴사 2

import sys

input = sys.stdin.readline

def run_program():
    N = int(input().strip())
    T = [0 for _ in range(N)]
    P = [0 for _ in range(N)]
    dp = [0 for _ in range(N)]
    for i in range(N): # T: 며칠동안, P: 이익
        T[i], P[i] = (map(int, input().strip().split()))
    
    # for i in range(N-1, -1, -1):
    #     # 1. 오늘 일해서 얻는 수익

run_program()

    

            
                    
