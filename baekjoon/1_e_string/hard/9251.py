import sys


input = sys.stdin.readline

def run_program():
    str_1 = input().strip()
    M = len(str_1)
    str_2 = input().strip()
    N = len(str_2)

    tablet = [[0 for _ in range(0, N+1)] for _ in range(0, M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if str_1[i-1] == str_2[j-1]:
                tablet[i][j] = tablet[i-1][j-1] + 1
            else:
                tablet[i][j] = max(tablet[i-1][j], tablet[i][j-1])

    print(tablet[M][N])

run_program()