input = [4, 6, 2, 9, 1]
# for i in range(1,5+1):
#     for j in range(1,i):
#         print(i-j)
# print()
def insertion_sort(array):
    for i in range(1, len(array) + 1):

        for j in range(1, i):
            if array[i-j-1]>array[i-j] :
                array[i-j-1],array[i-j]=array[i-j],array[i-j-1]
            else :
                break



insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!