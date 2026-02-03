import sys

input = sys.stdin.readline

def run_program():
    # 1. input 
    N = int(input().strip())
    data_days = {}
    data_profit = {}
    possible = {}
    for i in range(N):
        days, profit = map(int, input().strip().split())
        data_days[i+1] = days
        data_profit[i+1] = profit
        possible[i+1] = True
    
    # print(data_profit)
    # print(data_days)


    def get_profit(start, profit_now):
        if start > N:
            # print("profit_now:" + str(profit_now))
            return profit_now
        profit_max = -1
        for day_now in range(start, N+1):
            # 1. (가능하면) 스케줄에 표시
            if possible[day_now] and data_days[day_now] <= (N - day_now + 1): 
                for j in range(day_now, day_now + data_days[day_now]):
                    possible[j] = False
                # 2. profit_now update, 재귀해서 이 경우 최대 얻음
                profit_max_new = get_profit(day_now + 1, profit_now + data_profit[day_now])
                # 3. 현재 profit_max보다 큰가? 그러면 update
                if profit_max < profit_max_new:
                    profit_max = profit_max_new
                # 4. 스케줄 표시 취소
                for j in range(day_now, day_now + data_days[day_now]):
                    possible[j] = True

        if profit_max == -1:
            return profit_now
        else:
            return profit_max
    
    print(get_profit(1, 0))
    # print(possible)



run_program()