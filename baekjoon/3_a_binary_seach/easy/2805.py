import sys

input = sys.stdin.readline

def find_max(arr, M):
    left, right = 0, max(arr)
    while left <= right:
        mid = (left + right) // 2
        tree_sum = 0
        for tree in arr:
            if tree > mid:
                tree_sum += tree - mid
        if tree_sum < M: # 더 작은 높이로 잘라야..
            right = mid - 1
        else: # 더 큰 높이로 도전
            left = mid + 1

    # right < left
    # 가능 가능 가능 불가능 -> 따라서 right가 max의 값
    return right

def run_program():
    N, M = map(int, input().strip().split())
    tree_arr = list(map(int, input().strip().split()))
    print(find_max(tree_arr, M))

run_program()