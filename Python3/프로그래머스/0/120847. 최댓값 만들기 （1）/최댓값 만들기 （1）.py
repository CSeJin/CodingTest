def solution(numbers):
    a = max(numbers)
    numbers.pop(numbers.index(a))
    b = max(numbers)
    
    return a*b