shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

#가장 비싼 가격의 물건을 가장 할인률 높이자
#비싼 가격을 높은 할인률로 할인, 내림차순 정렬

def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_index = 0
    coupons_index = 0
    get_max_discounted_price= 0

    while price_index < len(prices) and coupons_index < len(coupons) :
        get_max_discounted_price += prices[price_index] * (100 - coupons[coupons_index])/100
        price_index += 1
        coupons_index += 1

    while price_index <len(prices):
        get_max_discounted_price += prices[price_index]
        price_index += 1
    return get_max_discounted_price

print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.