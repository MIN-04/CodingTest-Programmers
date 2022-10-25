# LEVEL 01 - 76501. 음양 더하기 (https://school.programmers.co.kr/learn/courses/30/lessons/76501)

def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for sign, absolute in zip(signs, absolutes))
