import sys

input = sys.stdin.readline
input_mult = sys.stdin.readlines

def run_program():
    S, E, Q = input().strip().split()
    attd = set()
    ans = 0
    for rl in input_mult():
        time, id = rl.strip().split()
        if time <= S:
            attd.add(id)
        elif E <= time <= Q and id in attd:
            attd.remove(id)
            ans += 1
    print(ans)

run_program()