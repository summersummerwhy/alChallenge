# 그 전거 기억하고 있다가... n
# 1. n-1 하나 작아졌다? 그러면 길이만큼 연속되는지 보기
# 2. 길이만큼 연속됐다? 그러면 1. 그 다음거 n-1이거나, 아예 업서가, 
# 3. n-2이다 -> 그러면 또 check 시작해야함


def check_path(arr, N, L):
    i = 1
    lamp = [False] * N
    while i < N:
        # print(i)
        if arr[i] == arr[i-1]:
            i += 1
        elif arr[i] == arr[i-1] + 1:
            # 연속 L개 존재 check
            if i - L < 0:
                return False
            # 연속 L개 같은 높이인지 check
            # i-L ~ i-1
            for j in range(i-L, i):
                if arr[j] != arr[i-1]:
                    return False
                if lamp[j]:
                    return False
                lamp[j] = True
            # 이어지는 높이 check -> 굳이 필요 없을듯?
            i += 1                
        elif arr[i] == arr[i-1] - 1:
            # 연속 L개 존재 check
            if i + L -1 >= N:
                return False
            # 연속 L개 같은 높이인지 check
            # i ~ i + L -1
            for j in range(i, i + L):
                if arr[j] != arr[i]:
                    return False
                lamp[j] = True
            # 이어지는 높이 check -> 얘도 굳이 필요 없을듯...?
            i = i + L
        else:
            return False
    return True
    
def run_program():
    N, L = map(int, input().split())
    paths = []
    for _ in range(N):
        paths.append(list(map(int, input().split())))
    for i in range(N):
        arr = []
        for j in range(N):
            arr.append(paths[j][i])
        paths.append(arr)
    ans = 0
    for p in paths:
        if check_path(p, N, L):
            ans += 1
    print(ans)


run_program()