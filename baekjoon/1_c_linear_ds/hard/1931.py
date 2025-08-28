import sys

input = sys.stdin.readline

def run_program():
    N = int(input().strip())
    sched = []
    for _ in range(N):
        new_sched = list(map(int, input().strip().split()))
        sched.append(new_sched)
    # 끝나는 시간 기준 (오름차순) 정렬
    sched.sort(key=lambda x: (x[1], x[0]))
    last = None
    result = 0
    for sch in sched:
        if last is None:
            last = sch
            result += 1
        else:
            if last[1] <= sch[0]:
                last = sch
                result += 1
    print(result)


run_program()