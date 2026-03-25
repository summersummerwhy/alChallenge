import sys
from itertools import combinations

input = sys.stdin.readline

def comb_10_i(i):
    def fact(j, n):
        count = 1
        ans = 1
        while count <= n:
            ans *= j
            j -= 1
            count += 1
        return ans

    if i > 5:
        return comb_10_i(10-i)
    else:
        return fact(10, i) // fact(i, i)
   

def run_program():
    N = int(input().strip())
    cards = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    card_num = 1
    comb_num = 1
    if N == 0:
        print(0)
    while N > 0:
        if card_num > 10:
            print(-1)
            break
        
        if card_num == 1:
            comb_num = 9
        else:
            comb_num = comb_10_i(card_num)

        if N <= comb_num:
            if card_num == 1:
                comb_num = 9
            else:
                comb_num = comb_10_i(card_num)
            cards = list(map(list, combinations(cards, card_num)))
            for i in range(len(cards)):
                cards[i].sort(reverse=True)
                cards[i] = int(''.join(cards[i]))
            cards.sort()
            if card_num == 1:
                print(cards[N])
            else:
                print(cards[N-1])
            break
        else:
            N -= comb_num
            card_num += 1
        
run_program()