import sys

input = sys.stdin.readline

def run_program():
    p_dict = {')': '(', ']': '['}
    wrong_dict = {')': '[', ']': '('}
    value_dict = {')': 2, ']': 3}
    command = input().strip()
    stack = []
    found_error = False
    for i in command:
        # print("i: " + i)
        if found_error:
            break
        elif i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            val = 0
            found_closing = False
            while len(stack) > 0:
                now = stack.pop()
                # print("now: "+str(now))
                if type(now) == int:
                    val += now
                elif now == wrong_dict[i]:
                    found_error = True
                    break
                elif now == p_dict[i]:
                    val *= value_dict[i]
                    found_closing = True
                    break
            if not found_closing:
                found_error = True
            else:   
                if val == 0:
                    stack.append(value_dict[i])
                else:
                    stack.append(val)
        # print(stack)
        
    result = 0
    if not found_error: 
        while len(stack) > 0:
            now = stack.pop()
            if type(now) == int:
                result += now
            else:
                result = 0
                break
   
    print(result)

run_program()
