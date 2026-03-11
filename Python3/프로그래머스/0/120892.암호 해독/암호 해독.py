# 방법 1
def solution(cipher, code):
    return ''.join(cipher[c] for c in range(code-1, len(cipher), code))

# 방법 2
def solution(cipher, code):
    return cipher[code-1::code]