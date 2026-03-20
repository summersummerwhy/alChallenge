import sys

input = sys.stdin.readline

# 1: 내구도 7, 무게 5
# 2: 내구도 3, 무게 4
# 1과 2 치면 1: 7-4, 2: 3-5 깨짐

# 계란: 최대 8개니까 모든 가능성 check하면 됨
# 순서는 정해져 있음
# visited대신 cracked로 check

def run_program():
    N = int(input().strip())
    durbl = []
    weight = []
    cracked = [False for _ in range(N)]

    for _ in range(N):
        a, b = map(int, input().strip().split())
        durbl.append(a)
        weight.append(b)

    max_count = 0
    
    def dfs(egg_now):
        nonlocal max_count
        if egg_now == N:
            count = cracked.count(True)
            if count > max_count: 
                max_count = count
            return
        
        if cracked[egg_now]:
            dfs(egg_now + 1)
        elif sum(cracked) == N-1:
            dfs(egg_now + 1)
        else:
            for i in range(N):
                if i != egg_now and not cracked[i]:
                    d, w, c_e, c_i = durbl[egg_now], durbl[i], cracked[egg_now], cracked[i]
                    # 지금 egg_now 부딪힐 계란 i
                    # update
                    durbl[egg_now] -= weight[i]
                    durbl[i] -= weight[egg_now]
                    if durbl[egg_now] <= 0:
                        cracked[egg_now] = True
                    if durbl[i] <= 0:
                        cracked[i] = True
                    dfs(egg_now + 1)
                    # update 취소
                    durbl[egg_now], durbl[i], cracked[egg_now], cracked[i] = d, w, c_e, c_i

    dfs(0)
    print(max_count)

run_program()


