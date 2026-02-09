import sys
from itertools import combinations
from math import inf

input = sys.stdin.readline

def run_program():
    # input 읽고 저장
    N, M = map(int, input().strip().split())
    city_map = []
    for _ in range(N):
        city_map.append(list(map(int, input().strip().split())))
    
    house_coor = []
    shop_coor = []
    house_shop_stat = []
    # 집 정보, 치킨집 정보 저장
    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 1: # 집 정보
                house_coor.append([i, j])
            elif city_map[i][j] == 2: # 치킨집 정보
                shop_coor.append([i, j])
    

    house_num = len(house_coor)
    shop_num = len(shop_coor)

    # 거리 계산해서 저장
    # i번째 house의 j번째 shop과의 거리: house_shop_stat[i][j]
    for i in range(house_num):
        arr_now = []
        for j in range(shop_num):
            stat = abs(house_coor[i][0] - shop_coor[j][0]) 
            stat += abs(house_coor[i][1] - shop_coor[j][1])
            arr_now.append(stat)
        house_shop_stat.append(arr_now)

    # M개 조합 후 치킨 거리 계산, 
    shop_comb = []
    for i in range(shop_num):
        shop_comb.append(i)
    
    # print(shop_num)
    # print(shop_comb)

    result_min = inf
    for comb in combinations(shop_comb, M):
        result_now = 0
        for i in range(house_num):
            stat_min = inf
            # 가장 짧은 거리 치킨 구하기
            for j in comb:
                if house_shop_stat[i][j] < stat_min:
                    stat_min = house_shop_stat[i][j]
            # 치킨거리에 더하기
            result_now += stat_min
        # 치킨거리 최소인지 확인하기
        if result_now < result_min:
            result_min = result_now


    print(result_min)
    

run_program()

