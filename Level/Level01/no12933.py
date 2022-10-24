# LEVEL 01 - 12933. 정수 내림차순으로 배치하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12933)

def solution(n):
    lst = list(str(n))
    lst.sort(reverse = True)
    return int(''.join(lst))
