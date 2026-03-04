def solution(num_list):
    mult, square = 1,0
    for i in num_list:
        mult *= i
    square = sum(i for i in num_list)**2
    return 1 if mult < square else 0