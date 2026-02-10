import sys

input = sys.stdin.readline

def run_program():

    K = int(input().strip())
    output_arr = []
    must_append = False

    if K <= 20:
        must_append = True
    
    def hanoi(from_b, to_b, num):
        nonlocal output_arr
        # base_case
        if num == 0:
            return
        else:
            empty_b = 6 - from_b - to_b
            # 하나 작은 탑을 남아있는 곳으로 옮기기 
            hanoi(from_b, empty_b, num-1)
            # 가장 큰것 목표하는 곳으로 옮기기
            print(f"{from_b} {to_b}")
            # 하나 작은 탑 목표하는 곳으로 옮기기
            hanoi(empty_b, to_b, num-1)
        
    print(2**K - 1)

    if must_append:
        hanoi(1, 3, K)

run_program()