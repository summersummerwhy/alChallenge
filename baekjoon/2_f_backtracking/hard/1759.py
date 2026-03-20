import sys

# 0. 일단 sort
# 1. L개짜리 조합 만들고
# 2. 조건 만족하는지 추측
#    근데 굳이 N개 됐을때 확인 안하고, 그 전에 확인??
#    아냐... 나중에 추가돼서 조건 만족할 수도

input = sys.stdin.readline



def possible(pw_list):
    v = 0
    c = 0
    vowel = {'a', 'e', 'i', 'o', 'u'}
    for i in pw_list:
        if i in vowel:
            v += 1
        else:
            c += 1
    return v >= 1 and c >= 2

def run_program():
    L, C = map(int, input().strip().split())
    letters = input().strip().split()
    letters.sort()

    path = []

    def dfs(start):
        if len(path) == L and possible(path):
            print(*path, sep = '')

        for i in range(start, C):
            path.append(letters[i])
            dfs(i+1)
            path.pop()
    
    dfs(0)

run_program()


