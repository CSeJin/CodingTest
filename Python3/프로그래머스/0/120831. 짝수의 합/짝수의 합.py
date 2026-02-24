def solution(n):
    if n <=0 or n > 1000:
        print("제한사항 오류")
        return
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer