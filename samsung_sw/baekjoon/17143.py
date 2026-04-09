# 100 * 10000
# ㅁ ㅁ ㅁ ㅁ ㅁ
# 거리: N의 배수 -> 위치 (N-i), 방향 반대
# 0 4 (방향 반대)
# 1 3 (방향 반대)
# 2 2
# 3 1
# 4 0 
# 거리: 2N의 배수 -> 위치 그대로, 방향 그대로

def move(i, j, R, C, s, d):
    # 위, 아래, 오른쪽, 왼쪽
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, 1, -1]
    left_dst = s
    if d <= 2:
        if (left_dst // (R-1)) % 2 == 1:
            d = 3 - d # 방향 전환
            i = (R-1) - i
        left_dst = left_dst % (R-1)
        first_dst = 0
        if d == 1:
            first_dst = i
        else:
            first_dst = R-1-i
        if left_dst < first_dst:
            i = i + dr[d] * left_dst
        else:
            i = i + dr[d] * first_dst
            d = 3-d # 방향 전환
            i = i + dr[d] * (left_dst - first_dst)
    else:
        if (left_dst // (C-1)) % 2 == 1:
            d = 7 - d # 방향 전환
            j = (C-1) - j
        left_dst = left_dst % (C-1)
        first_dst = 0
        if d == 4:
            first_dst = j
        else:
            first_dst = C-1-j
        if left_dst < first_dst:
            j = j + dc[d] * left_dst
        else:
            j = j + dc[d] * first_dst
            d = 7-d # 방향 전환
            j = j + dc[d] * (left_dst - first_dst)

    return d, i, j
            
# 1, 3 -> speed: 8 => size = 1 , 방향: 4: 왼쪽
# 3 2 1 0 1 2 3 4
def run_program():
    R, C, M = map(int, (input().split()))
    # id: 1~M
    sharks = [i for i in range(1, M+1)]
    coor = [[0] * 2 for _ in range(M+1)]
    speed = [0] * (M+1) # 속력
    direction = [0] * (M+1) # 방향
    size = [0] * (M+1) # 크기

    graph = [[0] * C for _ in range(R)]

    for i in range(M): 
        # id: i+1
        r, c, s, d, z = map(int, input().split())
        coor[i+1] = [r-1, c-1]
        speed[i+1] = s
        direction[i+1] = d
        size[i+1] = z
    # 상어의 아이디 list에 보관, 1~M까지 
    # 그걸 크기순으로 sort한다: 작은 것부터 움직이면 자연스럽게 잡아먹히게 할 수 있음
    sharks.sort(key=lambda x: size[x])
    ans = 0
    time = 0
    while time < C:
        # print(f"time: {time}")
        dead = []
        # 1. coor 정보대로 배치시킨다 (그대신 graph 다 0처리 해야함)
        for sh in sharks:
            r, c = coor[sh][0], coor[sh][1]
            if graph[r][c] != 0:
                # 해당 위치에 다른 상어 있는지 확인 -> 사망처리
                dead.append(graph[r][c])
            graph[r][c] = sh

        # 2. time의 column에 있는 상어 잡기
        for i in range(R):
            if graph[i][time] != 0:
                sh = graph[i][time]
                dead.append(sh)
                ans += size[sh]
                graph[i][time] = 0
                break

        # 죽은애들 update
        for sh in dead:
            sharks.remove(sh)

        # 3. 살아있는 상어들 이동시키기
        for sh in sharks:
            r, c = coor[sh][0], coor[sh][1]
            graph[r][c] = 0
            d, r, c = move(r, c, R, C, speed[sh], direction[sh])
            direction[sh], coor[sh][0], coor[sh][1] = d, r, c

        # 4 시간 update
        time += 1
    print(ans)

run_program()