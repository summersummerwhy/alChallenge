import sys


input = sys.stdin.readline


def run_program():
    N, K = map(int, input().strip().split())
    L = list(map(int, input().strip().split()))
    cnt = [0 for _ in range(100001)]
    left, right = 0, 0
    len_now = 0
    len_max = 0
    while True:
        if cnt[L[right]] == K:
            while cnt[L[right]] == K:
                cnt[L[left]] -= 1
                len_now -= 1
                left += 1
        cnt[L[right]] += 1
        len_now += 1
        len_max = max(len_now, len_max)
        # 다음 step
        right += 1
        if right == N:
            break

    print(len_max)

run_program()