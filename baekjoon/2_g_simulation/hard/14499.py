# 남쪽으로 굴리면 아래로 흐름
# 북쪽으로 굴리면 위로 흐름
# 동쪽으로 굴리면 오른쪽으로 흐름
# 서쪽으로 굴리면 왼쪽으로 흐름

#       0(뒤)
# 4(왼)  1(위) 5(와) (3(아래))
#       2(앞)
#       3(아래)
def roll_dice(dir, dice):
    dice_before = dice.copy()
    if dir == 1: # 동 
        dice[4] = dice_before[3]
        dice[1] = dice_before[4]
        dice[5] = dice_before[1]
        dice[3] = dice_before[5]
    elif dir == 2: # 서
        dice[4] = dice_before[1]
        dice[1] = dice_before[5]
        dice[5] = dice_before[3]
        dice[3] = dice_before[4]
    elif dir == 3: # 북
        dice[0] = dice_before[1]
        dice[1] = dice_before[2]
        dice[2] = dice_before[3]
        dice[3] = dice_before[0]
    else: # dir == 4 # 남
        dice[0] = dice_before[3]
        dice[1] = dice_before[0]
        dice[2] = dice_before[1]
        dice[3] = dice_before[2]
            


def run_program():
    dice = [0 for _ in range(6)]
    # 1: 동, 2: 서, 3: 북, 4: 남
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # 바닥의 수: dice[3]
    # 윗면의 수: dice[1]
    N, M, x, y, K = map(int, input().strip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().strip().split())))
    command = list(map(int, input().strip().split()))
    for i in command:
        next_x = x + dx[i-1]
        next_y = y + dy[i-1]
        if not (0 <= next_x < N and 0 <= next_y < M):
            continue
        # 지도로 이동
        x = next_x
        y = next_y
        # 주사위 굴리기
        roll_dice(i, dice)
        # 지도에 써있는 수 보고 주사위 바닥 변경
        if graph[x][y] == 0:
            graph[x][y] = dice[3]
        else:
            dice[3] = graph[x][y]
            graph[x][y] = 0
        # 위에 써있는 수 출력
        print(dice[1])

run_program()