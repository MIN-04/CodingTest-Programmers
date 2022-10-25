# LEVEL 01 - 70128. 내적 (https://school.programmers.co.kr/learn/courses/30/lessons/70128)

# 방법 1.
def solution(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))

# 방법 2.
def solution(a, b):
    return sum(i*j for i, j in zip(a, b))
