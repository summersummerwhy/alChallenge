import sys

input = sys.stdin.readline


# review:
# 1. 앞에서 부터 시작해도 상관없다
# 2. <조건을 만족하는 한> 가장 늦은/일찍 시작하는 것을 찾아내는 것
# <- 이 관점이 greedy
# 3. 한 원소를 기준으로 sort했다 -> 이러면 다른 원소의 순서는 보장 안됨!!

# "최소 갯수"
# [끝: 작 -> 큰] [시작: 작 -> 큰]
# 1. 끝나는 순서가 늦는 것대로 나열 (단, 3월 이후)
# 2. 그리고 가장 늦은 것부터 접근, <시작 날짜> 업데이트
# [가장 늦은 것] pop 
# 3. a. <시작 날짜>보다 일찍 끝난다 => 바로 끝내고 0 출력
#    b. <시작 날짜>보다 늦게 끝나는 것 있을 때까지 계속 pop (더 이른 시작 시간을 찾아), 
        #  안되면 마지막으로 pop한거에서 멈추기
        #  멈추고 + 1
# 4. 시작 날짜가 1, 2, 아니면 3월 1일이면 멈춘다


def run_program():
    N = int(input().strip())
    flowers = []
    for _ in range(N):
        a, b, c, d = map(int, input().strip().split())
        flowers.append([[a, b], [c,d]])
    start_now = [12, 1] # 현재 꽃이 피기 시작하는 날짜
    flowers.sort(key=lambda x: (x[1], x[0])) # (끝, 시),asc
    f_num = 0
    while start_now > [3, 1]:
        # 1. 꽃 부족 -> 0
        if len(flowers) == 0:
            f_num = 0
            break
        start, end = flowers.pop()
        start_min = start
        # 2. 빈틈 생김 -> 0
        if end < start_now:
            f_num = 0
            break
        # 3. 현재 시작 날짜보다 일찍 끝나는 꽃 나오거나 list 비면 break
        while True:
            if len(flowers) == 0 or flowers[-1][1] < start_now:
                break
            else: 
                start, end = flowers.pop()
                if start < start_min:
                    start_min = start
        f_num += 1
        start_now = start_min
    print(f_num)

run_program()