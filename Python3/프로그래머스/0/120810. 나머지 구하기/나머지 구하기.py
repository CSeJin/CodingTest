def solution(num1, num2):
    if num1 <=0 or num2 <=0 or num1 > 100 or num2 >100:
        print("제한사항 오류")
        return
    return num1 % num2

print(solution(101, 100))