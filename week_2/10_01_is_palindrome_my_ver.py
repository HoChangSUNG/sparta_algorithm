input = "abcba"


def is_palindrome(string):
    for index in range( len(string)//2+1 ) :
        if string[index]!=string[-(index+1)] :
            return False
    return True


print(is_palindrome(input))