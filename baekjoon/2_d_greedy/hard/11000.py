import sys
import heapq
input = sys.stdin.readline


def run_program():
    N = int(input().strip())
    lectures = []
    for _ in range(N):
        lectures.append(list(map(int, input().strip().split())))
    # 일찍 시작하는 순으로 정렬
    lectures.sort()
    rooms = [] 
    # 1. 끝나는 시간을 keep track한다는 idea
    # 2. 그 중에서도 가장 작은걸 알아야한다는 idea: "heap"
    # 3. 가장 작은걸 대체 (pop한후 heap에 추가)하면 된다는 idea: 
    #    why? 어차피 그 뒤에 오는 수업은 더 늦게 시작함, 빨리 끝나는거에 붙여야 빈틈이 최소화
    for l in lectures:
        # (가장 작은) 끝나는 시간이 지금 시작하는 시간보다 작아야한다
        if len(rooms) > 0 and rooms[0] <= l[0]:
            # 단순 대체 x, heap 형태 유지되어야 의미있음
            heapq.heappop(rooms)
            heapq.heappush(rooms, l[1])
        else:
            heapq.heappush(rooms, l[1])

    print(len(rooms))

run_program()
