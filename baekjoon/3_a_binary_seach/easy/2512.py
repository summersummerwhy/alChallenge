import sys

input = sys.stdin.readline

def find_max(bdg, arr):
    if sum(arr) <= bdg:
        return max(arr)
    left, right = 0, max(arr)
    while left <= right:
        mid = (left + right) // 2
        sum_bdg = 0
        for i in arr:
            if i > mid:
                sum_bdg += mid
            else: 
                sum_bdg += i
        if sum_bdg > bdg: # 예산 부족
            right = mid - 1
        else:
            left = mid + 1
    # right < left
    # 가능 가능 가능 불가능
    return right

def run_program():
    N = int(input())
    reg_arr = list(map(int, input().strip().split()))
    budget = int(input())
    print(find_max(budget, reg_arr))

run_program()