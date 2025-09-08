import sys
from collections import deque

input = sys.stdin.readline

def run_program():
    explode_str = input().strip()
    bomb_str = input().strip()
    bomb_len = len(bomb_str)
    bomb_cleared = False

    first_deque = deque([])
    second_deque = deque([])

    for char in explode_str:
        first_deque.append(char)

    while not bomb_cleared:
        bomb_cleared = False
        bomb_num = 0 
        from_deque = None
        to_deque = None

        if len(first_deque) > 0:
            from_deque = first_deque
            to_deque = second_deque
        else:
            from_deque = second_deque
            to_deque = first_deque

        while len(from_deque) > 0:
            char_now = from_deque.popleft()

            if char_now == bomb_str[-1] and len(to_deque) >= bomb_len - 1:
                is_bomb = True
                for i in range(len(bomb_str) - 1):
                    if bomb_str[-2 -i] != to_deque[-1 -i]:
                        is_bomb = False
                        break
                if is_bomb:
                    bomb_num += 1
                    for _ in range(bomb_len - 1):
                        to_deque.pop()
                else:
                    to_deque.append(char_now)
            else:
                to_deque.append(char_now)

        if bomb_num == 0:
            bomb_cleared = True
    
    if len(to_deque) == 0: 
        print("FRULA")
    else: 
        print(''.join(to_deque))
            
run_program()