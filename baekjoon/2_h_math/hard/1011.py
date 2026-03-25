import sys

input = sys.stdin.readline



def run_program():
    T = int(input().strip())
    for _ in range(T):
        x, y = map(int, input().strip().split())
        dist = y - x
        year = 0
        step = 1
        while dist > 0:
            if dist >= 2 * step:
                year += 2
                dist -= 2 * step
            elif dist > step:
                year += 2
                dist = 0
            else:
                year += 1
                dist = 0
            step += 1
        print(year)

run_program()

