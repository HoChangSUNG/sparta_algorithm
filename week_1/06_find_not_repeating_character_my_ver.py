input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurence_array= [0]*26
    for alphabet in string :
        index=ord(alphabet) - ord('a')
        alphabet_occurence_array[index] += 1

    for index in range(len(alphabet_occurence_array)) :
        if alphabet_occurence_array[index] == 1 :
            not_repeating_character = chr(index+ord('a'))
            return not_repeating_character

result = find_not_repeating_character(input)
print(result)