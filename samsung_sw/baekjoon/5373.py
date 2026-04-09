

# 6 3 0 # 시계방향: [col][2-row]
# 7 4 1          
# 8 5 2 

# 2 5 8 # 반시계방향: [2-col][row]
# 1 4 7
# 0 3 6 

def rotate(main_face, face_lst, idx_lst, clockwise):
    f_tmp = main_face.copy() 
    # main face 회전
    for t in range(9):
        r = t // 3
        c = t % 3
        if clockwise == '+':
            # A[c][2-r] = A[r][c]
            main_face[c * 3 + (2-r)] = f_tmp[t]
        else:
            # A[2-c][r] = A[r][c]
            main_face[(2-c) * 3 + r] = f_tmp[t]

    # 옆면 회전
    tmp = [i.copy() for i in face_lst] # 4개
    for i in range(4):
        j = -1
        if clockwise == '+': # 0 <- 3, 1 <-0
            j = (i + 3) % 4
        else:
            j = (i + 1) % 4
        for idx in range(3):
            face_lst[i][idx_lst[i][idx]] = tmp[j][idx_lst[j][idx]]

U = []
D = []
F = []
B = []
L = []
R = []

def initialize():
    global U, D, F, B, L, R
    U = ['w' for _ in range(9)]
    D = ['y' for _ in range(9)]
    F = ['r' for _ in range(9)]
    B = ['o' for _ in range(9)]
    L = ['g' for _ in range(9)]
    R = ['b' for _ in range(9)]

def cube_work(command):
    global U, D, F, B, L, R
    face = command[0]
    clockwise = command[1]
    main_face = []
    face_lst = []
    idx_lst = []
    if face == 'U':
        main_face = U
        # F[012], L[012], B[012], R[012] ->, <-
        face_lst = [F, L, B, R]
        idx_lst = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    elif face == 'D':
        main_face = D
        # F[678], R[678], B[678], L[678] ->, <-
        face_lst = [F, R, B, L]
        idx_lst = [[6, 7, 8], [6, 7, 8], [6, 7, 8], [6, 7, 8]]
    elif face == 'F':
        main_face = F
        # U[678], R[036], D[876], L[852] ->, <-
        face_lst = [U, R, D, L]
        idx_lst = [[6, 7, 8], [0, 3, 6], [6, 7, 8], [8, 5, 2]]
    elif face == 'B': 
        main_face = B
        # U[210], L[036], D[012], R[852]] ->, <-
        face_lst = [U, L, D, R]
        idx_lst = [[2, 1, 0], [0, 3, 6], [2, 1, 0], [8, 5, 2]]
    elif face == 'R':
        main_face = R
        # U[852], B[036], D[036], F[852] ->, <-
        face_lst = [U, B, D, F]
        idx_lst = [[8, 5, 2], [0, 3, 6], [0, 3, 6], [8, 5, 2]]
    else: 
        main_face = L
        # U[036], F[036], D[852], B[258] ->, <-
        face_lst = [U, F, D, B]
        idx_lst = [[0, 3, 6], [0, 3, 6], [8, 5, 2], [8, 5, 2]]
    rotate(main_face, face_lst, idx_lst, clockwise)


def print_face(Face):
    for i in range(3):
        print(*Face[i*3:i*3+3], sep='', end='\n')

def run_program():
    global U
    T = int(input())
    for _ in range(T):
        initialize()
        n = int(input())
        comm_lst = input().split()
        for comm in comm_lst:
            cube_work(comm)
        print_face(U)


run_program()



