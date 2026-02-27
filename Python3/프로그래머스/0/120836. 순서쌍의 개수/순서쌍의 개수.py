# 방법 1: O(n*n), 시간초과
def solution(n):
    list = [i for i in range(1, n+1)]
    return sum(1 for num in list for i in list if num*i == n)

# 방법 2
def solution(n):
    return sum(1 for i in range(1, n+1) if n % i ==0)

# 방법 3
def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer +=2
            if i*i == n:
                answer -= 1
    return answer
    