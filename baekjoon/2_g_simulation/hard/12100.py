import sys

input = sys.stdin.readline


def swipe(dir, board_in, N):
    board = [[0 for _ in range(N)] for i in range(N)]
    # Up
    if dir == 'U':
        for c in range(N):
            n_bf = -1
            r_now = 0
            has_added = True
            for r in range(N):
                n = board_in[r][c]
                # 0 임
                if n == 0:
                    continue
                # 직전 걸 막 추가했음
                elif has_added: 
                    n_bf = n
                    has_added = False
                    continue
                # 직전 것과 비교
                elif n_bf == n:
                    board[r_now][c] = 2 * n_bf
                    r_now += 1
                    has_added = True
                else:
                    board[r_now][c] = n_bf
                    n_bf = n
                    r_now += 1
                    has_added = False
            # 마지막 것 추가
            if not has_added:
                board[r_now][c] = n_bf
                r_now += 1         
    # Down
    elif dir == 'D':
        for c in range(N):
            n_bf = -1
            r_now = N-1
            has_added = True
            for r in range(N-1, -1, -1):
                n = board_in[r][c]
                # 0 임
                if n == 0:
                    continue
                # 직전 걸 막 추가했음
                elif has_added: 
                    n_bf = n
                    has_added = False
                    continue
                # 직전 것과 비교
                elif n_bf == n:
                    board[r_now][c] = 2 * n_bf
                    r_now -= 1
                    has_added = True
                else:
                    board[r_now][c] = n_bf
                    n_bf = n
                    r_now -= 1
                    has_added = False
            # 마지막 것 추가
            if not has_added:
                board[r_now][c] = n_bf
                r_now -= 1
    # Left
    elif dir == 'L':
        for r in range(N):
            n_bf = -1
            c_now = 0
            has_added = True
            for c in range(N):
                n = board_in[r][c]
                # 0 임
                if n == 0:
                    continue
                # 직전 걸 막 추가했음
                elif has_added: 
                    n_bf = n
                    has_added = False
                    continue
                # 직전 것과 비교
                elif n_bf == n:
                    board[r][c_now] = 2 * n_bf
                    c_now += 1
                    has_added = True
                else:
                    board[r][c_now] = n_bf
                    n_bf = n
                    c_now += 1
                    has_added = False
            # 마지막 것 추가
            if not has_added:
                board[r][c_now] = n_bf
                c_now += 1
    # Right
    else:
        for r in range(N):
            n_bf = -1
            c_now = N-1
            has_added = True
            for c in range(N-1, -1, -1):
                n = board_in[r][c]
                # 0 임
                if n == 0:
                    continue
                # 직전 걸 막 추가했음
                elif has_added: 
                    n_bf = n
                    has_added = False
                # 직전 것과 비교
                elif n_bf == n:
                    board[r][c_now] = 2 * n_bf
                    c_now -= 1
                    has_added = True
                else:
                    board[r][c_now] = n_bf
                    n_bf = n
                    c_now -= 1
                    has_added = False
            # 마지막 것 추가
            if not has_added:
                board[r][c_now] = n_bf
                c_now -= 1
    return board

def find_max(board, N):
    if N == 1:
        return board[0][0]
    max_num = -1
    for i in range(N):
        for j in range(N):
            if max_num < board[i][j]:
                max_num = board[i][j]
    return max_num


def run_program():
    N = int(input().strip())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip().split())))
    
    
    ans = 0

    def dfs(count, board_now):
        nonlocal ans
        if count == 5:
            max_now = find_max(board_now, N)
            if max_now > ans:
                ans = max_now
            return
        for dir in ['U', 'D', 'L', 'R']:
            dfs(count+1, swipe(dir, board_now, N))
    
    dfs(0, board)
    print(ans)

run_program()
