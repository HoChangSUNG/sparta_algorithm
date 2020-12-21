import queue

s = "(())()"


def is_correct_parenthesis(string):
    q=queue.Queue()
    for char in string : # 문자열의 맨 앞부터 queue로 입력
        q.put(char)

    count=0
    while q.qsize() >0 : # queue의 내부 값이 있는 동안
        if q.get() == '(' :
            count += 1
        else :
            count -= 1
        if count < 0 :
            return False # ')' 표시가 더 많고,')'가 맨 앞에 나왔을때
    if count != 0 : #맨 마지막 문자가 ')'가 아닐때
        return False
    return True



print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!