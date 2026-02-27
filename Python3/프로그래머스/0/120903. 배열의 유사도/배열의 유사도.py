def solution(s1, s2):
    return sum(1 for i in s1 for j in s2 if i==j)