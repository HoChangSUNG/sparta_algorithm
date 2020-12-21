input = [4, 6, 2, 9, 1]
# 1. [4 6 2 9 1]
#     - - - - -
# 2. [1 6 2 9 4]
#       - - - -
# 3. [1 2 6 9 4]
#         - - -
# 4. [1 2 4 9 6]
#           - -
# 5. [1 2 4 9 6](비교할필요 없음)
#             -
# 배열의 크기만큼 반복했다가  앞에서부터 한개씩 줄어들면서 반복하는 구조
# for i in range(5-1):     j=0   i=1     i=2      i=3
#     for j in range(5-i): j=0~4 j=0~3   j=0~2    j=0~1
#         print(i+j)       j=0~4 i+j=1~4 i+j=2~4  i+j=3~4

def selection_sort(array):#O(N^2)
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i],array[min_index] = array[min_index],array[i]
    return
selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

