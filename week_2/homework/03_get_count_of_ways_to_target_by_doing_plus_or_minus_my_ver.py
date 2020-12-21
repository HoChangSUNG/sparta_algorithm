numbers = [1, 1, 1, 1, 1]
target_number = 3
result=0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array,plus_or_minus_sum,index):
    if index==len(array)  :
        global target_number
        if target_number==plus_or_minus_sum :
            global result
            result+=1

        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array,plus_or_minus_sum+array[index],index+1)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array,plus_or_minus_sum-array[index],index+1)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers,0,0 ))  # 5를 반환해야 합니다!
print(result)