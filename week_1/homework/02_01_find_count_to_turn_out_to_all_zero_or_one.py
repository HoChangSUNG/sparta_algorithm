input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    to_zero=0
    to_one=0

    if string[0]=='0':
        to_one+=1
    if string[0]=='1':
        to_zero+=1
    for index in range(len(string)-1) :
        if string[index]!=string[index+1] :
            if string[index+1]=='0' :
                to_one+=1
            if string[index+1]=='1' :
                to_zero+=1
    print("to_zero : {}  to_one : {}".format(to_zero,to_one))
    return min(to_zero,to_one)





result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)