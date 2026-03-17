import sys

input = sys.stdin.readline

def run_program():
    # 읽기
    N, K = map(int, input().strip().split())
    units = [] # 오름 차순, 작은 순서대로
    for _ in range(N):
        units.append(int(input().strip()))

    ans = 0

    # 큰 금액부터 pop
    while len(units) > 0:
        unit_now = units.pop()
        if unit_now <= K:
            num = K // unit_now
            # update
            ans += num
            K -= num * unit_now

    print(ans)
    

run_program()