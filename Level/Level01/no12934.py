# LEVEL 01 - 12934. 정수 제곱근 판별 (https://school.programmers.co.kr/learn/courses/30/lessons/12934)

import math

def solution(n):
    if n < 0 or n % math.sqrt(n) != 0:
        return -1
    else:
        return int((math.sqrt(n) + 1) ** 2)
