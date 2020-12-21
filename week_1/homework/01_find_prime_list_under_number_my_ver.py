input = 20


def find_prime_list_under_number(number):
    prime_list=[]
    for num in range(number+1) :
        count=0
        for find_prime_check in range(1,num+1) :
            if(num%find_prime_check == 0) :
                count+=1
            elif count>2 :
                break
        if count==2 :
            prime_list.append(num)
    return prime_list


result = find_prime_list_under_number(input)
print(result)