# 방법 1
def solution(numbers):
    a = max(numbers)
    numbers.pop(numbers.index(a))
    b = max(numbers)
    
    return a*b

# 방법 2
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]