def solution(num_list):
    num = -1
    for n in num_list:
        if n < 0:
            num = num_list.index(n)
            break
    return num