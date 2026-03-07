# 방법 1
def solution(my_string, n):
    return my_string[(len(my_string)-n):]

# 방법 2
def solution(my_string, n):
    return my_string[-n:]