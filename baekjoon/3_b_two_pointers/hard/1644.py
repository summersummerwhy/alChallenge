import sys

input = sys.stdin.readline

# N보다 작거나 같은 소수 list 구하기
# 그 다음 two pointer식 계산 들어감

def get_primary_until(N):
    memo = [True] * (N+1)
    memo[0] = memo[1] = False
    for i in range(2, int(N**0.5)+1):
        if memo[i]:
            n = 2
            while i * n <= N:
                memo[i*n] = False
                n += 1

    return [i for i, prime in enumerate(memo) if prime]



def run_program():
    N = int(input())
    if N == 1:
        print(0)
        return
    pri_lst = get_primary_until(N)
    ans = 0
    left, right = 0, 0
    sum_now = pri_lst[0]
    while True:
        if sum_now >= N:
            if sum_now == N:
                ans += 1
            sum_now -= pri_lst[left] 
            left += 1
        elif right == len(pri_lst)-1:
            break
        else:
            right += 1
            sum_now += pri_lst[right]
    print(ans)

run_program()