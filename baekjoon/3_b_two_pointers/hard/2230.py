import sys
import math

input = sys.stdin.readline

# 즉
# 1. gap이 M보다 작다 -> right 늘리기
    # -> 늘리고? 하여간 right이 N 벗어나면 끝내기?
# 2. gap이 M보다 크다 (M이면 끝내기)
# 2-1. min에 update
# 2-2. left 제거하기



def run_program():
    N, M = map(int, input().strip().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    min_now = math.inf
    left = 0
    right = 1
    gap = arr[1] - arr[0]
    while True:
        while gap < M and right < N:
            right += 1
            if right == N:
                break
            gap = arr[right] - arr[left]
        if gap == M:
            min_now = gap
            break
        elif gap > M:
            min_now = min(min_now, gap)
            left += 1
            gap = arr[right] - arr[left]
        else: 
            break
    print(min_now)

run_program()