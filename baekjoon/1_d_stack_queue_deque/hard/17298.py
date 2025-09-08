import sys

input = sys.stdin.readline

def run_program():
    N = int(input().strip())
    array = list(map(int, input().strip().split()))
    stack = []
    result = []
    num_max = 0
    while len(array) > 0:
        num_now = array.pop()
        if num_max <= num_now or len(stack) == 0:
            stack = []
            result.append(-1)
            num_max = num_now
        else:
            found_max = False
            while not found_max:
                num_right = stack.pop()
                if num_right > num_now:
                    result.append(num_right)
                    stack.append(num_right)
                    found_max = True
        stack.append(num_now)
    while len(result) > 0:
        print(result.pop(), end=' ')    
run_program()