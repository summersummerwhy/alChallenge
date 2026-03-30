import sys

input = sys.stdin.readline

def find_max(arr, num):
    left, right = 1, max(arr)

    while left <= right:
        mid = (left + right) // 2

        sum = 0
        for l in arr:
            sum += l // mid
        if sum < num: # 더 작게 잘라야함
            right = mid - 1
        else: # 가능하다 -> 더 큰 값 탐색
            left = mid + 1
        # 가능하면 오른쪽으로 간다! -> 정답은 rigth
        # 마지막: right < left
        # 가능 가능 가능 불가능 -> 이렇게 가니까 right가 맞는 값
        # right: 마지막으로 가능했던 값
        # left: 처음으로 불가능했던 값

        
    return right

def run_program():
    K, N = map(int, input().strip().split())
    lan = []
    for _ in range(K):
        lan.append(int(input().strip()))
    print(find_max(lan, N))

run_program()