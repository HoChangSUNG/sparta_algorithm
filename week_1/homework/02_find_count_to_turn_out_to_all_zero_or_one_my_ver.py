from collections import deque
input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    to_all_zero_count = 0
    to_all_one_count = 0
    queue = deque(string)
    pre=queue.popleft()
    while queue :
        cur = queue.popleft()
        if pre != cur :
            if cur == '0' : # 1 -> 0
                to_all_zero_count +=1
            if cur == '1' : # 0 -> 1
                to_all_one_count += 1
        pre = cur
    if pre == '1': # string의 마지막 인덱스값이 1일때
        to_all_zero_count += 1
    if pre == '0' : # string의 마지막 인덱스값이 0일때
        to_all_one_count += 1

    print('to_zero : ', to_all_zero_count,'to_one : ', to_all_one_count)
    return min(to_all_zero_count,to_all_one_count)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)