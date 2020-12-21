input = "hello my name is sparta"


def find_max_occurred_alphabet(string):

    alphabet_occurence_array=[0]*26
    for char in string :
        if not char.isalpha():
            continue
        array_index=ord(char)-ord('a')
        alphabet_occurence_array[array_index]+=1

    max_index=0
    for index in range(len(alphabet_occurence_array)) :
        compare=alphabet_occurence_array[max_index]-alphabet_occurence_array[index]
        if compare<0 :
            max_index=index
    max_occurred_alphabet=chr(max_index+ord('a'))
    return max_occurred_alphabet

result = find_max_occurred_alphabet(input)
print(result)