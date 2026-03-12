def solution(myString):
    for s in myString:
        if ord(s.lower()) <= ord("l"):
            myString = myString.replace(s, 'l')
    return myString