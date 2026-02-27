# 방법 1: O(n*n), 시간초과
def solution(n):
    list = [i for i in range(1, n+1)]
    return sum(1 for num in list for i in list if num*i == n)

# 방법 2
def solution(n):
    list = [i for i in range(1, n+1)]
    return sum(1 for i in list if n % i ==0)
    