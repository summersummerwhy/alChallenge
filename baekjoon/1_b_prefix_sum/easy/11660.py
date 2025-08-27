import sys

input = sys.stdin.readline

def run_program():
    # input 받아서 저장해두기
    N, M = map(int, input().strip().split())
    matrix = [[0 for _ in range(N+1)]]
    psum = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(N):
        temp = list(map(int, input().strip().split()))
        temp.insert(0, 0)
        matrix.append(temp)
    x1_arr, y1_arr, x2_arr, y2_arr = [], [], [], []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().strip().split())
        x1_arr.append(x1)
        y1_arr.append(y1)
        x2_arr.append(x2)
        y2_arr.append(y2)    
    # 누적합 구하기
    for i in range(1, N+1):
        for j in range(1, N+1):
            psum[i][j] = psum[i][j-1] + psum[i-1][j] - psum[i-1][j-1] + matrix[i][j]
    # 누적값 계산해서 출력하기
    for i in range(M):
        x1, y1, x2, y2 = x1_arr[i], y1_arr[i], x2_arr[i], y2_arr[i]
        result = psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1]
        print(result)
run_program()