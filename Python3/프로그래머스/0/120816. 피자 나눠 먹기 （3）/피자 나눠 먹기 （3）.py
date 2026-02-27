# 방법 1
def solution(slice, n):
    return n//slice + (1 if n%slice!=0 else 0)

# 방법 2
def solution(slice, n):
    return (n-1)//slice +1