import sys

input = sys.stdin.readline

def run_program():
    N, M = map(int, input().strip().split())
    num_array = list(map(int, input().strip().split()))
    num_array.insert(0, 0)
    # 누적합 구해두기
    prefix_sum = [0 for _ in range(N+1)]
    prefix_sum[1] = num_array[1]
    for i in range(2, N+1):
        prefix_sum[i] = prefix_sum[i-1] + num_array[i]
    # input 받아서 output 계산해두기
    outputs = []
    for _ in range(M):
        a, b = map(int, input().strip().split())
        outputs.append(prefix_sum[b] - prefix_sum[a-1])
    # ouput 출력하기
    for i in range(M):
        print(outputs[i])

run_program()