import sys
import math

input = sys.stdin.readline


def run_program():
    T = int(input().strip())
    for i in range(T):
        N = int(input().strip())
        result = N
        appl = []
        for j in range(N):
            new_appl = list(map(int, input().strip().split()))
            appl.append(new_appl)
        # 서류 기준으로 (오름차순) 정렬
        appl.sort(key = lambda x: x[0])
        lowest_rank = math.inf
        # 앞에서부터 정렬하며 면접 lowest 기록
        for ppl in appl:
            if ppl[1] > lowest_rank:
                result -= 1
            if ppl[1] < lowest_rank:
                lowest_rank = ppl[1]
        # 최종 결과 출력 
        print(result)

run_program()


