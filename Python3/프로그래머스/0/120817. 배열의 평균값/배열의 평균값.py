# 방법 1
def solution(numbers):
    if min(numbers) < 0 or max(numbers) > 1000:
        print("숫자 크기 오류")
        return
    if len(numbers) < 1 or len(numbers) > 100:
        print("배열 크기 오류")
        return
    return sum(numbers) / len(numbers)