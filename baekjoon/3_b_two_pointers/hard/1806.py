import sys
import math

input = sys.stdin.readline


def run_program():
    N, S = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    if sum(arr) < S:
        print(0)
        return 
    left, right = 0, 0 
    len_min = math.inf
    len_now = 1
    sum_now = arr[0]
    while True:
        while sum_now < S:
            if right == N - 1:
                break
            right += 1
            len_now += 1
            sum_now += arr[right]
        if sum_now >= S:
            len_min = min(len_min, len_now)
            if len_min == 1:
                break
            sum_now -= arr[left]
            len_now -= 1
            left += 1
        else:
            break
    print(len_min)

run_program()
            
