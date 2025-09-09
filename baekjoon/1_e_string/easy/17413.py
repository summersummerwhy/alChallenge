import sys

input = sys.stdin.readline

def run_program():
    sentence = input().strip()
    words = []

    word = ''

    for i in range(len(sentence)):
        char = sentence[i]
        if char == '<' or char == '':
            words.append([False, word])
            word = ''
        elif char == '>':
            words.append([True, word])
            word = ''
        else:
            word += char
            if i == len(sentence) - 1:
                words.append([False, word])

    for word in words:
        if word[0] == True:
            print(f"<{word[1]}>", end='')
        else:
            chunks = word[1].split()
            for i in range(len(chunks)):
                if i == len(chunks) - 1:
                    print(chunks[i][::-1], end='')
                else:
                    print(chunks[i][::-1], end=' ')

run_program()