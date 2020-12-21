input = [1, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):

    answer=0
    for number in array :

        if answer*number>answer+number : # 두 수를 곱한 것이 두 수를 더한 것보다 클때
            answer*=number
        else : # 두 수를 곱한 것이 두 수를 더한 것보다 작거나 같을 때
            answer+=number
    return answer


result = find_max_plus_or_multiply(input)
print(result)