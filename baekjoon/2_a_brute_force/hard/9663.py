import sys

input = sys.stdin.readline

def run_program():
    # input 읽기
    N = int(input().strip())
    
    col_arr = [True] * N
    upright_arr = [True] * (2*N -1)
    downright_arr = [True] * (2*N-1)

    ans = 0

    def dfs(row):
        nonlocal ans
        if row == N:
            ans += 1
            return

        for col in range(N):
            upright = col - row + N - 1
            downright = col + row

            if col_arr[col] and upright_arr[upright] and downright_arr[downright]:
                col_arr[col] = False
                upright_arr[upright] = False
                downright_arr[downright] = False

                dfs(row + 1)

                col_arr[col] = True
                upright_arr[upright] = True
                downright_arr[downright] = True

    dfs(0)

    print(ans)

run_program()




