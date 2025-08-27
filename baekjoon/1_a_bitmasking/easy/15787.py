import sys

input = sys.stdin.readline

def run_program():
    numbers = input().strip().split()
    N = int(numbers[0])
    M = int(numbers[1])
    trains_status = []
    for _ in range(N):
        trains_status.append((1 << 25))
    for _ in range(M):
        command = input().strip().split()
        order = int(command[0]) 
        # train_num은 -1해서 0부터 센다
        train_num = int(command[1]) - 1
        x = -1
        if len(command) == 3:
            # 좌석 num도 -1해서 0부터샌다
            x = int(command[2]) - 1
        if order == 1:
            trains_status[train_num] |= (1 << x) 
        elif order == 2: 
            trains_status[train_num] &= ~(1 << x) 
        elif order == 3:
            trains_status[train_num] = trains_status[train_num] << 1
        elif order == 4: 
            trains_status[train_num] = trains_status[train_num] >> 1
            trains_status[train_num] |= (1 << 20) 
            trains_status[train_num] &= ~(1 << 19) 

    permitted = []
    for train in trains_status:
        train_str = bin(train)[-20:]
        new_pattern = True
        for p in permitted:
            if p == train_str:
                new_pattern = False
                break
        if new_pattern:
            permitted.append(train_str)
    
    print(len(permitted))

run_program()