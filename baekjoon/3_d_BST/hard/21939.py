import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def run_program():
    min_heap = [] # 작 (L, P)
    max_heap = [] # 큰 (-L, -P)
    solved = {}

    N = int(input())
    for _ in range(N):
        P, L = map(int, input().strip().split())
        heappush(min_heap, (L, P))
        heappush(max_heap, (-L, -P))
        solved[P] = False
    
    M = int(input())
    for _ in range(M):
        comm = list(input().strip().split())
        if comm[0] == "add":
            while solved[-max_heap[0][1]]:
                heappop(max_heap)
            while solved[min_heap[0][1]]:
                    heappop(min_heap)
            heappush(min_heap, (int(comm[2]), int(comm[1])))
            heappush(max_heap, (-int(comm[2]), -int(comm[1])))
            solved[int(comm[1])] = False
        elif comm[0] == "solved":
            solved[int(comm[1])] = True
        else:
            if comm[1] == "1":
                # 최대 출력
                while solved[-max_heap[0][1]]:
                    heappop(max_heap)
                # 문제 출력
                print(-max_heap[0][1])
            else:
                # 최대 출력
                while solved[min_heap[0][1]]:
                    heappop(min_heap)
                # 문제 출력
                print(min_heap[0][1])

run_program()

