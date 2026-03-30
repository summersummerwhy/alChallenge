import sys
import math

input = sys.stdin.readline

def find_min(sol):
    min_val = math.inf
    a, b = 0, 0
    left, right = 0, len(sol) - 1
    while left < right:
        sum_now = sol[left] + sol[right]
        if abs(sum_now) < min_val:
            min_val = abs(sum_now)
            a, b = sol[left], sol[right]
        if sum_now < 0:
            left += 1
        else:
            right -=1
    print(a, b)

def run_program():
    N = int(input())
    sol = list(map(int, input().strip().split()))
    find_min(sol)


run_program()