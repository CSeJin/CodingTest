# 방법 1
def solution(price):
    discount = 0.0
    if price >= 500000:
        discount = 0.2
    elif price >= 300000:
        discount = 0.1
    elif price >= 100000:
        discount = 0.05
    
    return int(price*(1-discount))

# 방법 2
def solution(price):
    discount = {500000: 0.2, 300000:0.1, 100000:0.05, 0:0.0}
    for discount_price, discount_rate in discount.items():
        if price >= discount_price:
            return int(price*(1-discount_rate))