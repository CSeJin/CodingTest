# 방법 1
def solution(array):
    array.sort()
    return array[len(array)//2]

# 방법 2
def solution(array):
    return sorted(array)[len(array)//2]