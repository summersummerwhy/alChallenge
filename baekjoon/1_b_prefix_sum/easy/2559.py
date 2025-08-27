import sys
import math

input = sys.stdin.readline

def run_program():
    N, K = map(int, input().strip().split())
    num_arr = list(map(int, input().strip().split()))
    num_arr.insert(0, 0)
    num_prefix = [0 for _ in range(N+1)]
    num_prefix[1] = num_arr[1]
    # 누적합 계산해두기
    for i in range(2, N+1):
        num_prefix[i] = num_prefix[i-1] + num_arr[i]
    # K개 연속 합 계산해두기 (i ~ i+(K-1)), 최댓값 기록
    sum_max = -math.inf
    for i in range (1, N-(K-1)+1):
        sum_now = num_prefix[i+(K-1)] - num_prefix[i-1]
        if sum_now > sum_max:
            sum_max = sum_now
    print(sum_max)

run_program()

