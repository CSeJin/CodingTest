def solution(num1, num2):
    if num1 >100 or num2 >100 or num1 >100 or num2 <= 0:
        print("제한사항 오류")
        return
    answer = int((num1/num2)*1000)
    return answer

print(solution(121,100))