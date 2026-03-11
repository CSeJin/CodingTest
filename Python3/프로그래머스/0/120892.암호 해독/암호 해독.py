def solution(cipher, code):
    return ''.join(cipher[c] for c in range(code-1, len(cipher), code)) 