# 방법 1
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

# 방법 2
def solution(my_string):
    answer = []
    for s in my_string:
        if ord(s) >= ord('A') and ord(s) <= ord('Z'):
            answer.append(chr(ord(s)+32))
        else:
            answer.append(s)
    return ''.join(sorted(answer))