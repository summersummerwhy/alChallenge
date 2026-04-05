# 가방 K개, 각각 담을 수 있는 무게 다름
# 1. 가방 작은 것부터 접근
# 2. 보석 현재 가방보다 작거나 같은거 maxheap에 넣는다
# 3. 그 다음 pop하기

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def run_program():
    N, K = map(int, input().strip().split())
    jewels = []
    bags = []
    for _ in range(N):
        m, v = map(int, input().strip().split())
        heappush(jewels, (m, v))
        
    for _ in range(K):
        bags.append(int(input()))

    # jewels 작은쪽부터....
    jewels.sort()
    bags.sort()

    ans = 0

    jewels_now = []
    
    for i in bags:
        # 현재 가방에 들어갈 무게보다 작은거 있으면 넣게
        while jewels and jewels[0][0] <= i:
            m, v = heappop(jewels)
            heappush(jewels_now, -v)
        

        if jewels_now:
            now = -heappop(jewels_now)
            ans += now
    
    print(ans)

run_program()

        
