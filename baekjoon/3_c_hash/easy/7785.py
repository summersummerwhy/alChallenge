import sys

input = sys.stdin.readline

def run_program():
    staff = set()
    n = int(input())
    for _ in range(n):
        name, bhv = input().strip().split()
        if bhv == "enter":
            staff.add(name)
        else: 
            staff.remove(name)
    
    result = list(staff)
    result.sort(reverse=True)
    print(*result, sep='\n')
    
run_program()