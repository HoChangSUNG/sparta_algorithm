from collections import deque

balanced_parentheses_string = "()))((()"
def balanced_or_correct_parentheses_return_and_check(string) :
    queue = deque(string)
    stack= []
    correct_check = True
    u = ""
    left, right = 0, 0
    while queue :
        char = queue.popleft()
        u+= char
        if  char == '(' :
            left +=1
            stack.append('s')
        else :
            right+=1
            if stack :
                stack.pop()
            else :
                correct_check = False
        if left ==right:
            break
    if len(stack) != 0 :
        correct_check =False
    return u,"".join(list(queue)),correct_check
def reversed_string(string) :
    reversed_string = ""
    for char in string :
        if char =='(':
            reversed_string += ')'
        else :
            reversed_string += '('
    return reversed_string
def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == "" :
        return ""
    else :
        u, v, is_correct = balanced_or_correct_parentheses_return_and_check(balanced_parentheses_string)
        print(u, v, is_correct)
        if is_correct :
            return u + get_correct_parentheses(v)
        else :
            return '('+get_correct_parentheses(v)+')'+reversed_string(u[1:-1])



print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!어야 합니다!