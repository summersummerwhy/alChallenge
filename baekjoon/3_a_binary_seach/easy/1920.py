import sys

input = sys.stdin.readline

def binary_search(x, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            print(1)
            return
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    print(0)
    return


def run_program():
    N = int(input().strip())
    N_lst = list(map(int, input().strip().split()))
    N_lst.sort()
    M = int(input().strip())
    M_lst = list(map(int, input().strip().split()))
    for x in M_lst:
        binary_search(x, N_lst)

run_program()