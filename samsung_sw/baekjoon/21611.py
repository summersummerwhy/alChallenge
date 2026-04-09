# 토네이도 모영 dictionary를 알려준다....
# 
# 좌표 -> index를 알려줌 (0에서부터 시작)
def tornado(N, graph):
    i, j = N//2, N//2
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    balls = []
    coor_idx = {}
    idx = 0
    # update 요소
    dir = 0
    length = 1
    repeated = 0
    step = 0 # 2번 반복
    while True:
        if idx > 0:
            coor_idx[(i, j)] = idx - 1
            if graph[i][j] > 0:
                balls.append(graph[i][j])
        # 다음 좌표로 이동
        i = i + dr[dir]
        j = j + dc[dir]
        idx += 1
        repeated += 1
        if not (0 <= i < N and 0 <= j < N):
            break
        # 요소 update
        if repeated == length:
            dir = (dir + 1) % 4
            repeated = 0
            step += 1
        if step == 2:
            length += 1
            step = 0
    return coor_idx, balls

def attack(i, j, d, s):
    dr = [None, -1, 1, 0, 0]
    dc = [None, 0, 0, -1, 1]
    count = 0
    victim = []
    while count < s:
        i += dr[d]
        j += dc[d]
        victim.append((i, j))
        count += 1
    return victim

def explode(balls, dead_set, exp_rec):
    repeat = True
    while repeat:
        exploded = False
        # 이제 4개 반복되는지 check
        i = 0
        last = -1
        count = 1
        while i < len(balls):
            now = balls[i]
            if i in dead_set:
                i += 1
                continue
            if last != now:
                # 예전거 (count개 동안 반복해서 추가)
                if count >= 4:
                    # last가 1이면 rec의 0번째...
                    exp_rec[last - 1] += count
                    back_count = 0
                    j = i - 1
                    while back_count < count:
                        if j not in dead_set:
                            back_count += 1
                            dead_set.add(j)
                        j -= 1
                    exploded = True
                # 이제 지금 읽은걸로 정보 변경
                count = 1
                last = now
            else:
                count += 1
            i += 1
        # list 마지막 부분 check
        if count >= 4:
            # last가 1이면 rec의 0번째...
            exp_rec[last - 1] += count
            back_count = 0
            j = i - 1
            while back_count < count:
                if j not in dead_set:
                    back_count += 1
                    dead_set.add(j)
                j -= 1
            exploded = True
        if not exploded:
            # 루프 탈출
            repeat = False            
    new_balls = []
    for idx in range(len(balls)):
        if idx not in dead_set:
            new_balls.append(balls[idx])
    return new_balls

def change(balls, max_num):
    if not balls:
        return []
    num_now = 0
    i = 1
    last = balls[0]
    count = 1
    new_balls = []
    while i < len(balls):
        now = balls[i]
        if last != now:
            new_balls.append(count)
            new_balls.append(last)
            num_now += 2
            if num_now == max_num:
                break
            count = 1
            last = now
        else:
            count += 1
        i += 1
    new_balls.append(count)
    new_balls.append(last)
    # N*N-1개를 넣어야되니까 : 0~N*N-2, max_num = N*N-1
    return new_balls[:max_num]


        
def run_program():
    N, M = map(int, input().split())
    graph = []
    command = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    for _ in range(M):
        command.append(list(map(int, input().split())))
    coor_idx, balls = tornado(N, graph)
    exp_rec = [0, 0, 0]
    for d, s in command:
        # 명령대로 공격, 피해리스트 받아오기
        victims = attack(N//2, N//2, d, s)
        dead_set = set()
        for r, c in victims:
            dead_set.add(coor_idx[(r, c)])
        balls = explode(balls, dead_set, exp_rec)
        balls = change(balls, N*N-1)
    print(exp_rec[0] + 2*exp_rec[1] + 3*exp_rec[2])

run_program()