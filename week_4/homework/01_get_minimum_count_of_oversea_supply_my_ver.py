
ramen_stock = 10
supply_dates = [4, 7 ,10, 15]
supply_supplies = [20,20, 5, 10]
supply_recover_k = 60


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    count=0
    dates_and_supply_dict ={}
    for i in range(len(supplies)) :
        dates_and_supply_dict[dates[i]] = supplies[i]
    sorted_dates_and_supply_dict=sorted(dates_and_supply_dict.items(), key = lambda item : item[1],reverse=True)
    print(sorted_dates_and_supply_dict)

    while stock < k :
        for key, value in sorted_dates_and_supply_dict:
            if key <= stock :
                stock += value
                sorted_dates_and_supply_dict.pop(0)
                count+=1
                break

    return count



print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))