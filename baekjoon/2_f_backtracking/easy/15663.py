import sys
from itertools import permutations

input = sys.stdin.readline

def run_program():
    N, M = map(int, input().strip().split())
    num = list(map(int, input().strip().split()))
    # 중복제거, 정렬
    num.sort()

    perm = list(permutations(num, M))
    visited = set()
    for p in perm:
        if p not in visited:
            visited.add(p)
            print(' '.join(map(str, p)))
    
run_program()