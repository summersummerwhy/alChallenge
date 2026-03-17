import sys

input = sys.stdin.readline

# 1. 양수의 경우:
    # 오른쪽에서부터 큰 순서대로 묶어야함....
# 2. 1의 경우
    # 더한다
# 3. 0: 일단 방치
# 4. 음수의 경우:
    # 왼쪽에서부터 두개씩 묶어야함 
    # 그리고 만약 하나가 남는다!
    # -> 0있는지 확인, 그러면 안더해도 되고
    # 0 없으면 더한다


# review: 이거 걍 0까지 한번에 넣으면 됨 
# 그리고 while문, pop()으로 더 깔끔한 코드 가능

def run_program():
    N = int(input().strip())
    minus = []
    zero_count = 0
    plus = []
    sum = 0
    for _ in range(N):
        n = int(input().strip())
        if n == 1:
            sum += 1
        elif n == 0:
            zero_count += 1
        elif n > 1:
            plus.append(n)
        else:
            minus.append(n)
    # 1. plus: 큰 순서대로 정렬
    plus.sort(key=lambda x: -x)
    if len(plus) %2 == 1:
        sum += plus.pop()
    former = 0
    for i in range(len(plus)):
        if i % 2 == 0:
            former = plus[i]
        else:
            sum += former * plus[i]
    # 2. minus: 작은 순서대로 정렬
    minus.sort()
    if len(minus) %2 == 1:
        if zero_count > 0:
            minus.pop()
        else:
            sum += minus.pop()
    for i in range(len(minus)):
        if i % 2 == 0:
            former = minus[i]
        else:
            sum += former * minus[i]
    
    print(sum)

run_program()