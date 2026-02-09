import sys
from itertools import combinations
from math import inf

input = sys.stdin.readline


def run_program():
    # input 처리
    S = []
    N = int(input().strip())
    members = []
    stats = []

    for i in range(N):
        S.append(list(map(int, input().strip().split())))
        members.append(i)

    # 가능한 stat의 수 비교하기
    for team in combinations(members, N//2):
        stat_now = 0
        for pair in combinations(team, 2):
            stat_now += S[pair[0]][pair[1]] 
            stat_now += S[pair[1]][pair[0]]
        stats.append(stat_now)
    
    # comb의 차 계산하기, 최소 찾아내기
    diff_min = inf
    for i in range(len(stats)//2):
        diff = abs(stats[i] - stats[len(stats)-1-i])
        if diff < diff_min:
            diff_min = diff

    print(diff_min)


run_program()

