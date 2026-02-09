import sys


def read_canto(N, tf):
    if tf == False:
        for _ in range(3**N):
            print(" ", end="")
    elif N == 0:
        print("-", end="")
    else:
        read_canto(N-1, True)
        read_canto(N-1, False)
        read_canto(N-1, True)


def run_program():
    for line in sys.stdin:
        N = int(line.strip())
        read_canto(N, True)
        print("")

run_program()