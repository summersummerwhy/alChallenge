import sys
import math

input = sys.stdin.readline

def run_program():
    n = int(input())
    sour = []
    bitter = []
    for _ in range(n):
        command = input().strip().split()
        sour.append(int(command[0]))
        bitter.append(int(command[1]))
    
    # 일단 모든 조합 넣은거 이진수로 표현하기
    ingred = (1 << n) - 1
    subset = ingred
    diff_min = math.inf
    
    while subset:
        # 현재 조합에서 신맛, 쓴맛 차이 
        sour_total = 1
        bitter_total = 0
        subset_bin_reversed = bin(subset)
        subset_bin = list(reversed(subset_bin_reversed))
        for i in range(len(subset_bin) - 2):
            if subset_bin[i] == '1':
                sour_total *= sour[i]
                bitter_total += bitter[i]
        diff = abs(sour_total - bitter_total)
        if (diff < diff_min):
            diff_min = diff
        # 다음 조합 계산
        subset = (subset - 1) & ingred
    
    print(diff_min)

run_program()