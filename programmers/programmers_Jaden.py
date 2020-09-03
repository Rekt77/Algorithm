def JadenCase(s):
    try:
        case = s[0].upper()+s.lower()[1:]
    except IndexError:
        case = s.upper()
    return case

def solution(s):
    corpus = map(JadenCase,s.split(" "))
    answer = " ".join(corpus)
    return answer