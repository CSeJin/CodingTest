# 방법 1
def solution(n):
    if n <=0 or n > 1000:
        print("제한사항 오류")
        return
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer

# 방법 2
def solution(n):
    return 2*(n//2)*((n//2)+1)/2

# 방법 3
def solution(n):
    return sum(i for i in range(2, n+1, 2))