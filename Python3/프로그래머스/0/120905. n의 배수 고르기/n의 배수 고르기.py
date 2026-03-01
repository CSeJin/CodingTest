# 방법 1
def solution(n, numlist):
    return [num for num in numlist if num%n==0]

# 방법 2
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))