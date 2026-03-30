import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

def find_max(arr):
    # a + b + c = d
    # a + b = d - c
    # 1. 모든 a + b를 구함 (중복 허용!)
    # 2. 이거 정렬
    # 3. d - c (d 큰 순서대로) 접근,
    # d 찾으면 바로 끝내기
    arr_ab = []
    for com in combinations_with_replacement(arr, 2):
        arr_ab.append(sum(list(com)))
    arr_ab.sort()
    # 모든 c에 대해 d는 위에서부터 접근, 찾으면 cont
    for d in range(len(arr)-1, 0, -1):
        for c in range(d):
            cur = arr[d] - arr[c]
            left, right = 0, len(arr_ab) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr_ab[mid] == cur:
                    return arr[d]
                if arr_ab[mid]  > cur:
                    right = mid - 1
                else:
                    left = mid + 1
    return -1 # 오차 방지




def run_program():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    print(find_max(arr))

run_program()