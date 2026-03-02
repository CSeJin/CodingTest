# 방법 1
def solution(num_list):
    even_odd = [0,0]
    for num in num_list:
        if num%2==0:
            even_odd[0] += 1
        else:
            even_odd[1] += 1
    return even_odd
    
# 방법 2
def solution(num_list):
    odd_num = sum(1 for num in num_list if num%2 != 0)
    return [len(num_list)-odd_num, odd_num]

# 방법 3
def solution(num_list):
    li = [0,0]
    for num in num_list:
        li[num%2] += 1
    return li