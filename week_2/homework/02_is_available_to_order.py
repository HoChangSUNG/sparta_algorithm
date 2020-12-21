shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders): # O((M+N) * logN)
    shop_menus.sort()  # 정렬의 시간 복잡도는 배열의 길이(N)
                       # O(N * logN)
    for order in orders:# M(orders가 바뀔 수 있으므로) -> O(M * logN)
        if not is_existing_target_number_binary(order, menus) :# O(log N)
            return False

    return True

def is_existing_target_number_binary(target, array):
    current_min=0
    current_max=len(array)-1
    current_guess= (current_min+current_max)//2

    while current_min<=current_max:
        if array[current_guess] ==target :
            return True
        elif array[current_guess] <target:
            current_min=current_guess+1
        else :
            current_max=current_guess-1
        current_guess = (current_min + current_max) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)