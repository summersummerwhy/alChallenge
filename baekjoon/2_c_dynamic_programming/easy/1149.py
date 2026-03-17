import sys

input = sys.stdin.readline

# R: 0, G: 1, B: 2

def run_program():
    N = int(input().strip())
    rgb_cost = []
    rgb_min = []
    for _ in range(N):
        rgb_cost.append(list(map(int, input().strip().split())))
        rgb_min.append([0, 0, 0])
    # print(rgb_cost)
    for i in range(N):
        if i == 0:
            rgb_min[0] = rgb_cost[0].copy()
        else:
            rgb_min[i][0] = min((rgb_min[i-1][1], rgb_min[i-1][2])) + rgb_cost[i][0]
            rgb_min[i][1] = min((rgb_min[i-1][0], rgb_min[i-1][2])) + rgb_cost[i][1]
            rgb_min[i][2] = min((rgb_min[i-1][0], rgb_min[i-1][1])) + rgb_cost[i][2]
    print(min(rgb_min[N-1]))

run_program()