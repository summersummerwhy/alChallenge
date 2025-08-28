import sys

input = sys.stdin.readline

def combination_2(num):
    return (num * (num-1)) // 2

def run_program():

    N, M = map(int, input().strip().split())
    num_arr = list(map(int, input().strip().split()))
    num_arr.insert(0, 0)
    psum_arr = [0 for _ in range(N+1)]
    mod_arr = [0 for _ in range(N+1)]
    mod_cnt_arr = [0 for _ in range(M)]

    for i in range(1, N+1):
        psum_arr[i] = psum_arr[i-1] + num_arr[i]
    for j in range(N+1):
        mod_arr[j] = psum_arr[j] % M
        mod_cnt_arr[mod_arr[j]] += 1
    
    result = 0

    for i in range(M):
        if mod_cnt_arr[i] > 1:
            result += combination_2(mod_cnt_arr[i])
    
    print(result)

run_program()
