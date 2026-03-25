import sys

input = sys.stdin.readline

def partial_fact(num, t):
    ans = 1
    num_now = num
    while t > 0:
        ans *= num_now
        num_now -= 1
        t -= 1
    return ans

def NCK(n, k):
    if k > n // 2:
        return NCK(n, n-k)
    return (partial_fact(n, k) // partial_fact(k, k)) % 10007


def run_program():
    N, K = map(int, input().strip().split())
    print(NCK(N, K))

run_program()
