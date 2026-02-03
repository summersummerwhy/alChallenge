import sys

input = sys.stdin.readline

pn_list = None

def run_program():
    # test cases
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        pn_list = []
        is_steady = True
        for i in range(n):
            pn_now = input().strip()
            if not is_steady:
                break
            for pn in pn_list:
                if pn.find(pn_now) == 0 or pn_now.find(pn) == 0:
                    is_steady = False
                    break
        if is_steady:
            print("YES")
        else:
            print("NO")

    



