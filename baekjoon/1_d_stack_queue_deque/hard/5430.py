import sys
from collections import deque

input = sys.stdin.readline

def run_program():
    N = int(input().strip())
    for _ in range(N):
        has_error = False
        r_cnt = 0
        command = input().strip()
        num = int(input().strip())
        temp = input().strip().strip('[]').split(',')
        queue = deque(list(temp), maxlen=num)
        for char in command:
            if char == 'D':
                if len(queue) == 0:
                    print("error")
                    has_error = True
                    break
                else:
                    if r_cnt % 2 == 0:
                        queue.popleft()
                    else:
                        queue.pop()
            elif char == 'R':
                r_cnt += 1
        if r_cnt % 2 == 1:
            queue.reverse()
        if not has_error:
            print("["+",".join(map(str, queue))+"]")
    
run_program()
