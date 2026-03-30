import sys

input = sys.stdin.readline

def run_program():
    N, d, k, c = map(int, input().strip().split())
    sushi = []
    all_menu = [0 for _ in range(d+1)]
    for _ in range(N):
        sushi.append(int(input()))

    # N-1, 0, 1 , 2
    # N-3, N-2, N-1, 0 
    # i - N + 4개 더 필요
    # i, (i+1) % N, (i+2) % N, (i+3) % N
    max_num = 0
    num_now = 0
    for i in range(k):
        if all_menu[sushi[i]] == 0:
            max_num += 1
        all_menu[sushi[i]] += 1
    num_now = max_num
    if all_menu[c] == 0:
        max_num += 1
    for i in range(N-1):
        # 슬라이딩 윈도우
        # left sushi 빼기: i (0 ~ N-2)
        all_menu[sushi[i]] -= 1
        if all_menu[sushi[i]] == 0:
            num_now -= 1
        # right sushi 더하기: (i+k)% N (4)
        if all_menu[sushi[(i+k)%N]] == 0:
            num_now += 1
        all_menu[sushi[(i+k)%N]] += 1

        # max update
        if all_menu[c] == 0:
            max_num = max(max_num, num_now + 1)
        else:
            max_num = max(max_num, num_now)

    print(max_num)

run_program()  
        

