# 방법 1
def solution(array, height):            
    answer = 0
    
    for i in range(len(array)):
        if height < array[i]:
            answer+=1
    return answer

# 방법 2
def solution(array, height):
    return sum(1 for x in array if x > height)

# 방법 3
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)