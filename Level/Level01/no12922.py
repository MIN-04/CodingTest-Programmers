# LEVEL 01 - 12922. 수박수박수박수박수박수? (https://school.programmers.co.kr/learn/courses/30/lessons/12922)


# 방법 1.
def solution(n):
    s = "수박" * n
    return s[:n]
    
# 방법 2.
def solution(n):
    return ''.join('수박'[i%2] for i in range(n))
