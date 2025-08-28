import sys
import math

input = sys.stdin.readline

def run_program():
    # input 저장
    N, M = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.insert(0, 0)
    psum = [0 for _ in range(N+1)]
    # 누적합 계산
    for i in range(1, N+1):
        psum[i] = psum[i-1] + arr[i]
    
    len_min = math.inf
    found_min = False

    if psum[N] >= M:
        for len in range(1, N+1):
            for idx in range(1, (N+1)-len+1):
                sum_now = psum[idx + len - 1] - psum[idx - 1]
                # print(f"len:{len}  idx:{idx} sum_now:{sum_now}")
                if sum_now >= M:
                    len_min = len
                    found_min = True
                    break
            if found_min:
                break
        print(len_min)
    else:
        print(0)

run_program()