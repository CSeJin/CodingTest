def solution(dot):
    x, y = dot[0], dot[1]
    answer = 0
    
    if x*y > 0:
        answer = 1 if x>0 else 3
    else:
        answer = 2 if x<0 else 4
    
    return answer