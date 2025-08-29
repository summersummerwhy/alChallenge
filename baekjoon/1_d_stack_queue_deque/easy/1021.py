import sys
import math
from collections import deque

input = sys.stdin.readline


class RotatingQueue:
    
    def __init__(self, N):
        temp = []
        for i in range(1, N+1):
            temp.append(i)
        self.queue = deque(temp, maxlen=N)
        self.len = N
        self.move_count = 0
    
    def dequeue(self):
        if (self.len > 0):
            self.len -= 1
            return self.queue.popleft()
        else:
            return None
        
    def move_left(self):
        if (self.len > 0):
            self.queue.append(self.queue.popleft())
            self.move_count += 1
    
    def move_right(self):
        if (self.len > 0):
            self.queue.appendleft(self.queue.pop())
            self.move_count += 1
    
    def get_index(self, num):
        idx = self.queue.index(num)
        return idx + 1
    
def run_program():
    N, M = map(int, input().strip().split())
    goal = list(map(int, input().strip().split()))
    rq = RotatingQueue(N)

    for i in goal:
        idx = rq.get_index(i)
        if idx <= math.ceil(rq.len / 2):
            for _ in range(idx - 1):
                rq.move_left()
        else:
            for _ in range(rq.len - idx + 1):
                rq.move_right()
        
        rq.dequeue()

    print(rq.move_count)


run_program()