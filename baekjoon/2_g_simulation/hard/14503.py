import sys

input = sys.stdin.readline


# 북 -> 서: 0 -> 3
# 동 -> 북: 1 -> 0
# 남 -> 동: 2 -> 1
# 서 -> 남: 3 -> 2
def run_program():
    # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
    # [row, column] (where to move next)
    move = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    N, M = map(int, input().strip().split())
    r_now, c_now, dir_now = map(int, input().strip().split())
    # -1: 청소됨, 0: 청소 X됨, 1: 벽 
    room = []
    for _ in range(N):
        room.append(list(map(int, input().strip().split())))

    def out_of_room(row, col):
        return not (0 <= row < N and 0 <= col < M)

    def is_all_clean():
        for i in move.values():
            row = r_now + i[0]
            col = c_now + i[1]
            if out_of_room(row, col):
                continue
            if room[row][col] == 0:
                return False
        return True
    
    cnt = 0
        
    while True:
        # 1. 현재칸 청소 X -> 청소
        if room[r_now][c_now] == 0:
            room[r_now][c_now] = -1
            cnt += 1
        # 2. 현재칸 청소 O
        elif is_all_clean():
            #   2-1. 주변 4칸 다 청소 O 
            #      if 바라보는 방향 유지 후진 X: 작동 멈추기
            #      else: 후진
            row_next = r_now - move[dir_now][0]
            col_next = c_now - move[dir_now][1]
            if out_of_room(row_next, col_next):
                break
            elif room[row_next][col_next] == 1:
                break
            else:
                r_now = row_next
                c_now = col_next
        else:
            dir_now = (dir_now + 3) % 4
            row_next = r_now + move[dir_now][0]
            col_next = c_now + move[dir_now][1]
            if out_of_room(row_next, col_next):
                continue
            elif room[row_next][col_next] == 0:
                r_now = row_next
                c_now = col_next

    print(cnt)

run_program()



    







 