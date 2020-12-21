input = [3, 5, 6, 1, 2, 4]


def is_number_exist_first(number, array):#첫번째 방법

    if number in array :
        return True
    else :
        return False


def is_number_exist_second(number,array) : #두번째 방법

    for value in array :
        if number==value :
            return True
    else :
        return False

result_first = is_number_exist_first(100, input)
result_second = is_number_exist_second(1, input)
print(result_first)
print(result_second)