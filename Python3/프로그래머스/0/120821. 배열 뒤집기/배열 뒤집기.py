# 방법 1
def solution(num_list):
    answer = []
    for i in range(len(num_list)-1, -1, -1):
        answer.append(num_list[i])
    return answer

# 방법 2
def solution(num_list):
    return num_list[::-1]

# 방법 3
def solution(num_list):
    answer =[]
    while(num_list):
        answer.append(num_list.pop())
    return answer

# 방법 4
def solution(num_list):
    num_list.reverse()  # reverse()는 리턴이 null
    return num_list