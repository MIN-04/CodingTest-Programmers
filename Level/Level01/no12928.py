# LEVEL 01 - 12928. 약수의 합 (https://school.programmers.co.kr/learn/courses/30/lessons/12928)

def solution(n):
    # n / 2 의 수들만 검사
    return n + sum(i for i in range(1, n // 2 + 1) if n % i == 0)
   
