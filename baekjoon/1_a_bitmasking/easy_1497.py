import sys
import math

input = sys.stdin.readline

def run_program():
    numbers = input().strip().split()
    guitar_num = int(numbers[0])
    song_num = int(numbers[1])
    info_bit_list = []

    # 기타별 곡 정보 비트로 변환 후 저장
    for _ in range(guitar_num):
        command = input().strip().split()
        info_str = command[1]
        info_bit = (1 << song_num) - 1
        for i in range(song_num):
            letter = info_str[i]
            if letter == 'N':
                info_bit &= ~(1 << i) 
        info_bit_list.append(info_bit)
    
    # 곡 정보의 모든 조합 확인하며 최대한 많은 곡, 최소 수 구하기
    max_song_num = -math.inf
    min_guitar_num = math.inf

    song_all = 0
    guitar_all = (1 << guitar_num) - 1
    subset = guitar_all

    # 모든 조합 돌기
    while subset:
        current_song_bit = song_all
        current_guitar_num = 0
        for i in range(len(bin(subset))-2):
            if subset & (1 << i) == 1 << i:
                current_guitar_num += 1
                current_song_bit |= info_bit_list[i]
        # current_song_bit에서 song_num 확인하기
        current_song_num = bin(current_song_bit).count('1')

        # update
        if current_song_num > max_song_num:
            max_song_num = current_song_num
            min_guitar_num = current_guitar_num
        elif current_song_num == max_song_num:
            if current_guitar_num < min_guitar_num:
                min_guitar_num = current_guitar_num

        # 다음 조합
        subset = (subset - 1) & guitar_all
    
    # 조합 순회 후 출력
    if max_song_num == 0:
        print(-1)
    else:
        print(min_guitar_num)


run_program()
