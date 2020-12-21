input = [4, 6, 2, 9, 1]
# [4,6,2,9,1]
# ->->->->
# [4,2,6,1,9]
# ->->->
# [2,4,1,6,9]
# ->->
# [2,1,4,6,9]
# ->
# [1,2,4,6,9]
#4번만 반복되면 됨
    # for i in range(5-1) : 4번 반복됨
    #     for j in range(5-1-i):
    #         print j
# 배열의 크기 -1 만큼 반복했다가 한개씩 줄어들면서 반복
def bubble_sort(array):#O(N^2)
    n=len(array)
    for i in range(n-1) :
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!