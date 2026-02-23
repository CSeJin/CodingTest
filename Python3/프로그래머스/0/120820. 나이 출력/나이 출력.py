def solution(age):
    if age >120 or age <= 0:
        print("제한사항 오류")
        return
    answer = 2022 - age + 1
    return answer

print(solution(121))