import sys


input = sys.stdin.readline

class CS:
    def __init__(self, len=0, seq=''):
        self.len = len
        self.seq = seq
    
    def get_max(other1, other2):
        if other1.len > other2.len:
            return other1
        else:
            return other2

def run_program():
    str_1 = input().strip()
    M = len(str_1)
    str_2 = input().strip()
    N = len(str_2)

    tablet = [[CS() for _ in range(0, N+1)] for _ in range(0, M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if str_1[i-1] == str_2[j-1]:
                tablet[i][j].len = tablet[i-1][j-1].len + 1
                tablet[i][j].seq = tablet[i-1][j-1].seq + str_1[i-1]
            else:
                tablet[i][j] = CS.get_max(tablet[i-1][j], tablet[i][j-1])

    print(tablet[M][N].len)
    if (tablet[M][N].len > 0):
        print(tablet[M][N].seq)

run_program()
