import sys

input = sys.stdin.readline


def pow_recursive(a, b, c):
    if b == 1:
        return a % c
    else: 
        half = pow_recursive(a, b//2, c)
        result = half * half % c
        if b % 2 == 0:
            return result
        else:
            return (result * (a % c)) % c


def run_program():
    A, B, C = map(int, input().strip().split())
    print(pow_recursive(A, B, C))



    
run_program()
