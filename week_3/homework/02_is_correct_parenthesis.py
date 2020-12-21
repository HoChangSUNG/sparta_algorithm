input = "(())()"
# 1. ( 괄호 열림
# 2. ( ( 괄호 열림
# 3. ) 괄호 닫힘 아까 열린 것 중에 현재 괄호는 (
# 4. ) 괄호 닫힘 아까 열린 것 중에 현재 괄호는
# 5. ( 괄호 열림
# 6. ) 괄호 닫힘 아까 열린 것 중에 현재 괄호는
# 올바른 괄호쌍
#
# ((()
# 1. ( 괄호 열림
# 2. ( ( 괄호 열림
# 3. ( ( (괄호 열림
# 4. ) 괄호 닫힘 아까 열린 것 중에 현재 괄호는 ( (
# 올바르지 않은 괄호쌍
def is_correct_parenthesis(string):
    stack=[]
    for i in range(len(string)) :
        if string[i] == "(" :
            stack.append(i) #어떤 값 들어가도 상관x(담겨 있는지 여부만 확인하면 됨)
        elif string[i] == ")" :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()
    if len(stack) == 0 :
        return True
    else :
        return False



print(is_correct_parenthesis(input))  # True 를 반환해야 합니다!  # 결과로 [4, 1, 3, 0] 가 와야 합니다!