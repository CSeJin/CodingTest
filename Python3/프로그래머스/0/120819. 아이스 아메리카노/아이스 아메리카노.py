# 방법 1
def solution(money):
    return [money//5500, money%5500]

# 방법 2
def solution(money):
    return list(divmod(money, 5500))