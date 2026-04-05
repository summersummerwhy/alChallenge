import sys
import heapq

input = sys.stdin.readline

def clean_heap(h, deleted):
    # heap의 우선순위 중 방문한게 있으면 삭제
    while h and deleted[h[0][1]]:
        heapq.heappop(h)



def run_program():
    T = int(input())
    for _ in range(T):
        k = int(input())
        deleted = [False] * k
        min_heap = []
        max_heap = []
        for i in range(k): # i: id 취급
            comm, num = input().strip().split()
            num = int(num)
            if comm == "I":
                heapq.heappush(min_heap, [num, i])
                heapq.heappush(max_heap, [-num, i])
            else:
                if num == -1:
                    # 최솟값 삭제
                    clean_heap(min_heap, deleted)
                    if min_heap:
                        n, id = heapq.heappop(min_heap)
                        deleted[id] = True
                else: 
                    # 최댓값 삭제
                    clean_heap(max_heap, deleted)
                    if max_heap:
                        n, id = heapq.heappop(max_heap)
                        deleted[id] = True
        clean_heap(min_heap, deleted)
        clean_heap(max_heap, deleted)
        if min_heap or max_heap:
            max_now = -heapq.heappop(max_heap)[0]
            min_now = heapq.heappop(min_heap)[0]
            print(max_now, min_now)
        else:
            print("EMPTY")

run_program()