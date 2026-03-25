import sys
input = sys.stdin.readline

def run_program():
    A, B = map(int, input().split())

    limit = int(B ** 0.5)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    i = 2
    while i * i <= limit:
        if is_prime[i]:
            j = i * i
            while j <= limit:
                is_prime[j] = False
                j += i
        i += 1

    ans = 0
    for p in range(2, limit + 1):
        if is_prime[p]:
            temp = p * p
            while temp <= B:
                if temp >= A:
                    ans += 1
                temp *= p

    print(ans)

run_program()