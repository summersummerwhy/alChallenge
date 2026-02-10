import sys

input = sys.stdin.readline


def identity_matrix(N):
    result = [[0 for _ in range(N)]for j in range(N)]
    for i in range(N):
        result[i][i] = 1
    return result

def multiply_matrix(A, B):
    N = len(A)
    result = [[0 for _ in range(N)]for j in range(N)]
    for i in range(N): # 행
        for j in range(N): # 열
            sum = 0
            for k in range(N): # 곱해서 더하는 entry
                sum += A[i][k] * B[k][j] % 1000
            result[i][j] = sum % 1000
    return result

def pow_matrix(A, N):
    # 기초 케이스
    if N == 0:
        return identity_matrix(len(A))
    else: 
        half = pow_matrix(A, N//2)
        double_half = multiply_matrix(half, half)
        if N % 2 == 1:
            return multiply_matrix(double_half, A)
        else: 
            return double_half
def run_program():
    N, B = map(int, input().strip().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().strip().split())))

    result = pow_matrix(A, B)
    for arr in result:
        for entry in arr:
            print(entry, end = " ")
        print("")


run_program()


