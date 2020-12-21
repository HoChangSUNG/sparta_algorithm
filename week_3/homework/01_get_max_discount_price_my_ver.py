shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    discount_price=0
    coupons.sort(reverse=True) #coupons 배열 내림차순 정렬
    prices.sort(reverse=True) #prices 배열 내림차순 정렬

    for idx in range(0, len(prices)) :
        if idx<len(coupons): # 큰 가격에 큰 할인율이 적용되도록
            discount_price+= (prices[idx] * ((100-coupons[idx]) / 100))
        else : #할인율이 적용되지 않는 경우
            discount_price+=prices[idx]
    return discount_price

print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.