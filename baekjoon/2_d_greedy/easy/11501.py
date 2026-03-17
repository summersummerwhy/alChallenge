import sys

input = sys.stdin.readline

# 1. 뒤에서부터 가격 알려줌
# 2. max 주기적 update
# 3. max보다 작다? 그러면 차세 이익 더함

def run_program():
    # input
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        stocks = list(map(int, input().strip().split()))
        max_st = 0
        profit = 0
        while len(stocks) > 0:
            now_st = stocks.pop()
            if now_st > max_st:
                max_st = now_st
            else:
                profit += max_st - now_st
        # answer
        print(profit)

run_program()
