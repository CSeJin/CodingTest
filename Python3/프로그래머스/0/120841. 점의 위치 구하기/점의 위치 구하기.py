# 방법 1
def solution(dot):
    x, y = dot
    if x*y > 0:
        return 1 if x>0 else 3
    else:
        return 2 if x<0 else 4
    
# 방법 2
def solution(dot):
    quad = [(2,3),(1,4)]
    return quad[dot[0] > 0][dot[1] < 0]