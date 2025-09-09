import sys

input = sys.stdin.readline

def run_program():
    address_lst = input().strip().split(':')
    complete_lst = []
    insert_num = 8 - len(address_lst) + address_lst.count('')
    insert_done = False
    for i in range(len(address_lst)):
        temp_num = address_lst[i]
        if temp_num == '':
            if not insert_done:
                for _ in range(insert_num):
                    complete_lst.append('0000')
                insert_done = True
        else:
            if len(temp_num) < 4:
                for _ in range(4 -len(temp_num)):
                    temp_num = '0' + temp_num
            complete_lst.append(temp_num)

    print(':'.join(complete_lst))

run_program()

