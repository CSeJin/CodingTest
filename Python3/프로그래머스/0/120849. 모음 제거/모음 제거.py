def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u'] 
    return ''.join(c for c in my_string if c not in vowels)