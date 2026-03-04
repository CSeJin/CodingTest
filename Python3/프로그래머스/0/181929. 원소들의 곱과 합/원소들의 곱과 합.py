# 방법 1
def solution(num_list):
    mult, square = 1,0
    for i in num_list:
        mult *= i
    square = sum(i for i in num_list)**2
    return 1 if mult < square else 0

# 방법 2
def solution(num_list):
    s = sum(num_list)**2
    m = eval('*'.join(str(i) for i in num_list))
    return 1 if s > m else 0