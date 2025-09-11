import sys

input = sys.stdin.readlines

def run_program():
    html_input = input()
    lines = []
    for i in html_input:
        i = i.strip()
        if len(i) > 0:
            temp = i.split()
            for j in temp:
                lines.append(j)

    words = []
    len_now = 0
    for i in lines:
        if i == '<br>':
            print(' '.join(words))
            words = []
            len_now = 0
        elif i == '<hr>':
            if len(words) > 0:
                print(' '.join(words))
                words = []
                len_now = 0
            print('-'*80)
        else:
            # 현재 단어 포함 길이 판단
            if len_now == 0:
                len_now += len(i)
            else:
                len_now += 1 + len(i)

            # 더 길면? 미리 출력
            if len_now > 80:
                print(' '.join(words))
                words = []
                # 길이 지금 단어 길이로 reset
                len_now = len(i)

            # 어쨌든 지금 단어는 지금 print하지 않는다
            words.append(i)

    if len(words) > 0:
        print(' '.join(words))
    
run_program()