import sys
from collections import deque

input = sys.stdin.readline


def run_program():
    n, w, L = map(int, input().strip().split())
    trucks = deque(list(map(int, input().strip().split())))
    queue = deque([0 for _ in range(w)], maxlen=w)
    sum_w = 0
    clock = 0
    truck_count = 0
    while truck_count < n:
        # 트럭 나오기
        if queue[0] > 0:
            sum_w -= queue[0]
            truck_count += 1
        # 트럭 집어넣을지 판단
        if len(trucks) > 0 and trucks[0] + sum_w <= L:
            # 트럭 집어넣기
            sum_w += trucks[0]
            queue.append(trucks.popleft())
        else:
            # 트럭 안 집어넣기
            queue.append(0)
        # print(queue)
        clock += 1
    
    print(clock)
            
run_program()
