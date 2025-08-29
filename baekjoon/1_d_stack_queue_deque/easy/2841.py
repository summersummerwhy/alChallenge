import sys

input = sys.stdin.readline


def run_program():
    N, M = map(int, input().strip().split())
    finger = [[] for _ in range(N+1)]
    move_count = 0

    for _ in range(N):
        melody, fret = map(int, input().strip().split())
        while len(finger[melody]) > 0 and finger[melody][-1] > fret:
            # 손가락 떼기
            finger[melody].pop()
            move_count += 1
        if len(finger[melody]) == 0 or finger[melody][-1] < fret:
            # 손가락 누르기
            finger[melody].append(fret)
            move_count += 1
    
    print(move_count)

run_program()