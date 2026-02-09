from itertools import permutations
import math
import sys

input = sys.stdin.readline

def calculate(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        if a < 0:
            return -(-a//b)
        else:
            return a//b

def run_program():
    # 1. input 읽어내기
    N = int(input().strip())
    num_list = list(map(int, input().strip().split()))
    oper_count = list(map(int, input().strip().split()))
    oper_type = [0, 1, 2, 3]
    oper_list = []
    for i in range(4):
        for j in range(oper_count[i]):
            oper_list.append(oper_type[i])

    
    # 2. 조합하기
    ans_max = -math.inf
    ans_min = math.inf
    for result in permutations(oper_list, N-1):
        # 첫번째 숫자
        int_now = num_list[0]
        for i in range(N-1):
            int_now = calculate(int_now, num_list[i+1], result[i])
        
        ans = int_now

        if ans > ans_max:
            ans_max = ans
        if ans < ans_min:
            ans_min = ans

    print(ans_max)
    print(ans_min)


    

run_program()


# for result in permutations(["+", "+", "-"], 3):
#     print(result)
#     print(type(result))

# print(type(eval("1+2")))