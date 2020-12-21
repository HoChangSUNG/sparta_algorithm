input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    i=0
    while i<len(array)-1 :

        for index in range(len(array)-1-i) :

            if array[index]>array[index+1]:
                array[index], array[index+1]=array[index+1],array[index]

        i += 1


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!