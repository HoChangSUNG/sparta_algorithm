# 문제 설명
# 1. 각 바게트 빵의 길이를 담은 배열이 주어진다.
# 2. 손님은 바게트 빵의 길이로 원하는 양을 요구한다.
# 3. 이 때, 길이만 고려하고 조각 수는 고려하지 않는다.
# 4. 바게트 빵 자르는 기계는 작두처럼 한 번에 모든 바게트 빵을 자를 수가 있습니다.
# 5. 자르고 남은, 일정하지 않은 부분들을 가져다가 팝니다!!!
# Q. 이 때 손님이 원하는 양을 주기 위해 설정해야 하는 길이의 최댓값은?
#
# Ex)
# 바게트 빵의 갯수와 각 빵의 길이 : [11, 17, 13, 15]
# 손님이 원하는 양: 8
# => 높이 15로 잘랐을 때, 얻을 수 있는 빵의 길이 = [0, 2, 0, 0] 의 합
# => 2
# => 높이 10으로 잘랐을 때, 얻을 수 있는 빵의 길이 = [1, 7, 3, 5] 의 합
# => 16
# 답 : 12
#
# < 주의점 및 팁 >
# :질문:튜터님! 12로 자르면 [0, 5, 1, 3]의 합이라서 9만큼 주는데요 :질문:
# => 답변 : 13으로 자르면 [0, 4, 0, 2]의 합이라서 6밖에 안 나와서 12가 답 입니다!
# => 더 줘도 되지만 덜 주면 안됩니다!
# => 즉, 가장 조금 더 주는 경우를 고려하시면 됩니다!

def baguette_slice(array,need) :
    start = 0
    end = max(array)
    baguette_amount=0
    mid = (start+end) // 2
    while start <= end :
        baguette_amount = 0
        for arr in array :
            if arr - mid >0 :
                baguette_amount += (arr - mid)
        if baguette_amount >= need :
            start=mid+1
        else :
            end=mid-1
        mid = (start + end) // 2

    return mid

array=[11,17,13,15]
need=8

baguette_slice(array,need)
