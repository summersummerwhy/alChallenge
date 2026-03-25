import sys
from itertools import combinations


input = sys.stdin.readline

def aCb(a, b):
    def fact(j, n):
        count = 1
        ans = 1
        while count <= n:
            ans *= j
            j -= 1
            count += 1
        return ans

    if b > a // 2:
        return aCb(a, a-b)
    else:
        return fact(a, b) // fact(b, b)


def run_program():
    N, M, K = map(int, input().strip().split())
    if K > aCb(N + M, N):
        print(-1)
        return
    N_cnt = N
    M_cnt = M
    while M_cnt > 0 and N_cnt > 0:
        # a로 시작하는 경우의 수
        cnt = aCb(M_cnt + N_cnt - 1, N_cnt - 1)
        if K <= cnt:
            print('a', end = '')
            N_cnt -= 1
        else:
            print('z', end = '')
            K -= cnt
            M_cnt -= 1
    
    print('a' * N_cnt + 'z' * M_cnt)

run_program()
