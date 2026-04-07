import math

# N개 시험장, i번에 Ai명
# 총: B명, 부: C명
# 각 시험장에 총은 1명 부는 여러명

def run_program():
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    ans = 0
    for st in A:
        st_now = st - B
        ans += 1
        if st_now > 0:
            ans += math.ceil(st_now / C)
    print(ans)

run_program()