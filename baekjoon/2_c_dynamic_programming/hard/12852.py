import sys


input = sys.stdin.readline

# 그러니까 특정 숫자까지 가는 최소 계산수를 세고
# 그 다음수: /3 가능하면 그 횟수 +1, /2 가능하면 그 횟수 +1, 1보다 크거나 같으면 그 횟수 + 1
# 해서 그 최소수를 update하면 되는거지... N이 될때까지

def run_program():
    N = int(input().strip())
    memoiz = [[-1, 0] for _ in range(N+1)] # [0: 그 전 수, 1: 지금까지 횟수] 
    for i in range(2, N+1):
        candidates = []
        if i % 3 == 0:
            candidates.append([i//3,  memoiz[i//3][1]])
        if i % 2 == 0:
            candidates.append([i//2, memoiz[i//2][1]])
        candidates.append([i-1, memoiz[i-1][1]]) # [지금 수, 지금까지의 횟수]

        # print(i)
        # print(candidates)

        if len(candidates) == 1:
            memoiz[i] = [candidates[0][0], candidates[0][1] + 1]
        else:
            winner = min(candidates, key=lambda k: k[1])
            memoiz[i] = [winner[0], winner[1] + 1]
        

        # print(memoiz[i])



    print(memoiz[N][1])
    now = N
    while now >= 1:
        print(now, end=' ')
        now = memoiz[now][0] # 그 전 숫자
    print()

run_program()