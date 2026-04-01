import sys

input = sys.stdin.readline
# 1. 1종류 있을때 (n+1)C1 - 1
# 2. 2종류 있을때 (n+1)C1*(m+1)C1 - 1

def run_program():
    n = int(input())
    for _ in range(n):
        m = int(input())
        closet = {}
        for i in range(m):
            name, tp = input().strip().split()
            if tp in closet:
                closet[tp].append(name)
            else:
                closet[tp] = [name]
        ans = 1
        for _, value in closet.items():
            ans *= (len(value) + 1)
        ans -= 1
        print(ans)
run_program()