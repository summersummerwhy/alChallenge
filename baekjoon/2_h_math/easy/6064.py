import sys

input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcs(m, n):
    return m * n // gcd(m, n)



def run_program():
    T = int(input().strip())
    for _ in range(T):
        M, N, x, y = map(int, input().strip().split())
        lcs_mn = lcs(M, N)
        i = 0
        found = False
        while True:
            k = M * i + x
            if k > lcs_mn:
                print(-1)
                break
            if (k - y) % N == 0:
                print(k)
                break
            i += 1
        

run_program()