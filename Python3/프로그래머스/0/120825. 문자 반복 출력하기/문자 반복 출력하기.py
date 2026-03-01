# 방법 1
def solution(my_string, n):
    repeated_string = ''
    for c in my_string:
        repeated_string += c*n
    return repeated_string