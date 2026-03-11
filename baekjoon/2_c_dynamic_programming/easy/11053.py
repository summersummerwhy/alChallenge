import sys

input = sys.stdin.readline

# 얘 다시 풀어야 할듯....
def run_program():
    N = int(input().strip())
    num_arr = list(map(int, input().strip().split()))
    memo_arr = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if num_arr[j] < num_arr[i]:
                memo_arr[i] = max(memo_arr[j] + 1, memo_arr[i])

    print(max(memo_arr))


                    
run_program()
