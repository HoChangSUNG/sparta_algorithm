array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    index_1 = 0
    length_1 = len(array1)

    index_2 = 0
    length_2 = len(array2)

    merge_array = []

    while index_1 < length_1 and index_2 < length_2 :
        if array1[index_1] >= array2[index_2] :
            merge_array.append(array2[index_2])
            index_2 += 1
        else :
            merge_array.append(array1[index_1])
            index_1 += 1

    if index_1 == len(array1) :
        for index in range(index_2, len(array2)) :
            merge_array.append(array2[index])

    elif index_2 == len(array2) :
        for index in range(index_1, len(array1)) :
            merge_array.append(array1[index])
    return merge_array
print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!