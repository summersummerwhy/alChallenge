import sys

input = sys.stdin.readline

def run_program():
    def add(S, x):
        S = S | (1 << x)
        return S

    def remove(S, x):
        S = S & ~(1 << x)
        return S

    def toggle(S, x):
        S = S ^ (1 << x)
        return S

    def all(S):
        S = (1 << 21) - 1
        return S

    def empty(S):
        S = 0
        return S

    def check(S, x):
        if (S & (1 << x)):
            print(1)
        else:
            print(0)

    n = int(input())
    S = 0
    for _ in range(n):
        command = input().strip().split()
        if command[0] == "add":
            S = add(S, int(command[1]))
        elif command[0] == "remove":
            S = remove(S, int(command[1]))
        elif command[0] == "check":
            check(S, int(command[1]))
        elif command[0] == "toggle":
            S = toggle(S, int(command[1]))
        elif command[0] == "all":
            S = all(S)
        elif command[0] == "empty":
            S = empty(S)
    
run_program()