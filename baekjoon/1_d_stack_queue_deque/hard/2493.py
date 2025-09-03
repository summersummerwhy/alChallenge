import sys
from collections import deque

input = sys.stdin.readline


def run_program():
    N = int(input().strip())
    heights = list(map(int, input().strip().split()))
    temp = []
    for i in range(N):
        temp.append([i+1, heights[i]])
    towers = deque(temp)
    stack = deque()
    max_height = 0
    while len(towers) > 0:
        tower_now = towers.popleft()
        if tower_now[1] > max_height:
            max_height = tower_now[1]
            stack.clear()
            print(0, end=" ")
        else:
            found_max = False
            while not found_max:
                tower_next = stack.pop()
                if tower_next[1] > tower_now[1]:
                    found_max = True
                    stack.append(tower_next)
                    print(tower_next[0], end=" ")
        stack.append(tower_now)

run_program()

