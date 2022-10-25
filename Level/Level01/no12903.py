# LEVEL 01 - 12903. 가운데 글자 가져오기 (https://school.programmers.co.kr/learn/courses/30/lessons/12903)

def solution(s):
    q = len(s) // 2
    r = len(s) % 2
    return s[q - 1 + r : q + 1]
