import sys
from itertools import combinations

input = sys.stdin.readline

def get_num(n, A, m, B, T):
    # 1. A, B에 대해 가능한 모든 조합의 합을 구하고, 합에 대한 조합의 수도 정리한다
    # 2. 그걸 array에 보관, 정렬
    # 3. 걍 하나씩 이동시키면 되지 않나?
    # A는 작은것부터 접근, B는 큰것부터 접근, T - A[i]보다 B[j]가 작으면 멈추고 다시 올라감
    A_sum, B_sum = [], []
    A_sum_cnt, B_sum_cnt = {}, {}
    # -> 여기서 굳이 set 안사용하고 list 사용해도 될듯
    for sum_lst, sum_cnt, N, lst in (A_sum, A_sum_cnt, n, A), (B_sum, B_sum_cnt, m, B):
        for i in range(0, N): # 0 ~ N
            for j in range(i+1, N+1): # 1 ~ N+1
                sum_now = sum(lst[i:j])
                if sum_now not in sum_cnt:
                    sum_cnt[sum_now] = 1
                    sum_lst.append(sum_now)
                else:
                    sum_cnt[sum_now]+= 1
    A_sum.sort()
    B_sum.sort()
    i = 0
    j = len(B_sum) - 1
    ans = 0

    while i < len(A_sum) and j >= 0:
        sub = T - A_sum[i]
        while j >= 0 and B_sum[j] >= sub:
            if B_sum[j] == sub:
                ans += A_sum_cnt[A_sum[i]] * B_sum_cnt[B_sum[j]]
            j -= 1
        i += 1
    return ans
    

def run_program():
    T = int(input())
    n = int(input())
    A = list(map(int, input().strip().split()))
    m = int(input())
    B = list(map(int, input().strip().split()))
    print(get_num(n, A, m, B, T))

run_program()

