import sys

input = sys.stdin.readline


def run_program():
    A, B, C = map(int, input().strip().split())

    num_now = 1
    # 제곱한 후 패턴 찾기
    pattern = []

    while True:
        num_now *= A % C
        num_now %= C
        if pattern.count(num_now) != 0:
            break
        pattern.append(num_now)

    # 패턴 길이 확보
    pattern_len = len(pattern)- pattern.index(num_now)
    result = num_now

    for _ in range(B % pattern_len):
        result *= A % C
        result %= C

    print(result)


    
run_program()
