def solution(num_list):
    li = ['','']
    for i in num_list:
        li[i%2] += str(i)
    ev = int(li[0]) if li[0] else 0
    od = int(li[1]) if li[1] else 0
    return ev + od
    