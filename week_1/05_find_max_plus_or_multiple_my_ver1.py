input = [1, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):

    for index in range(0,len(array)-1) :
        if array[index]<2 or array[index+1]<2 :
            array[index+1]=array[index]+array[index+1]
        else :
            array[index + 1] = array[index] * array[index + 1]
    return array[len(array)-1]
result = find_max_plus_or_multiply(input)
print(result)