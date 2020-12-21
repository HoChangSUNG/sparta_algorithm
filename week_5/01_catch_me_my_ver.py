from collections import deque

c = 11
b = 2
memo={ # 브라운이 시간에 따라 위치할 수 있는 위치를 저장. 0 : [2] -> 0초 때 2에 위치

}
def n_second_after_brown_position(n,memo) :
    if n in memo : #0초일때 브라운의 위치
        return

    memo[n]=list()
    for memo_value in memo[n - 1] : # 브라운의 시간에 따른 위치가 0 이상 200000 이하 일때만 memo에 저장
        if memo_value - 1 not in memo[n] and 0 <= memo_value - 1 <= 200000:
            memo[n].append(memo_value - 1)
        if memo_value + 1 not in memo[n] and 0 <= memo_value + 1 <= 200000:
            memo[n].append(memo_value + 1)
        if memo_value * 2 not in memo[n] and 0 <= memo_value * 2 <= 200000:
            memo[n].append(memo_value * 2)




def catch_me(cony_loc, brown_loc):
    queue= deque()
    queue.append(cony_loc)
    second = 0
    memo[second] = [brown_loc]  #0초일때 브라운의 위치 저장
    while queue :
        n_second_after_brown_position(second, memo) # 브라운이 n초에 위치할 수 있는 위치들을  memo에 저장
        cony_loc = queue.popleft()
        # print(second,"초에 코니의 위치 : ",cony_loc,second,"초에 브라운의 위치" ,memo[second])

        if  0 <= cony_loc <= 200000 and cony_loc in memo[second] : # 따라 잡았을 때
            return second
        elif cony_loc>200000 : # 코니가 도망치는데 성공했을 때
            return -1 #코니가 도망치는데 성공했을 때
        second += 1
        queue.append(cony_loc + second)





print(catch_me(c, b))  # 5가 나와야 합니다!