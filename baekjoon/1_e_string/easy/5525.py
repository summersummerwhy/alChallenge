import sys
import math

input = sys.stdin.readline

def run_program():
    N = int(input().strip())
    M = int(input().strip())
    p_str = input().strip()
    p_len = 2*N + 1
    result = 0
    idx = 0
    success_idx = -math.inf

    while idx <= M - p_len:
        gap = 1
        if p_str[idx] == 'I':
            has_p_str = True
            starting_i = 1
            if idx == success_idx + 2:
                starting_i = 2*N -1
            for i in range(starting_i, 2*N + 1):
                if i % 2 == 1:
                    if p_str[idx + i] != 'O':
                        has_p_str = False
                        gap = i
                        break
                elif p_str[idx + i] != 'I':
                    has_p_str = False
                    gap = i + 1
                    break
            if has_p_str:
                result += 1
                gap = 2
                success_idx = idx
        idx += gap
    
    print(result)

run_program()



