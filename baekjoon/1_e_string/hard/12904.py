import sys

input = sys.stdin.readline

def run_program():
    S = input().strip()
    T = input().strip()

    while len(T) > len(S):        
        if T[-1] == 'A':
            T = T[:-1]
        else: # B
            T = T[:-1]
            T = T[::-1]
    
    # print(T)
    if S == T:
        print(1)
    else:
        print(0)

run_program()