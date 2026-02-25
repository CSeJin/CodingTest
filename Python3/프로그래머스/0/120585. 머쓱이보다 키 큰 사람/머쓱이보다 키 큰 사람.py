# 방법 1
def solution(array, height):            
    answer = 0
    
    for i in range(len(array)):
        if height < array[i]:
            answer+=1
    return answer

# 방법 2
#def solution(array, height):
    