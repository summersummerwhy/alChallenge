import sys

input = sys.stdin.readline


def find_cnt(A, N, M):
    sum_now = 0
    cnt = 0 
    left, right = 0, 0
    while True:
        if sum_now >= M:
            if sum_now == M:
                cnt += 1
            sum_now -= A[left]
            left += 1
        elif right == N:
            break
        else:
            sum_now += A[right]
            right += 1

    return cnt

def run_program():
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    print(find_cnt(A, N, M))

run_program()