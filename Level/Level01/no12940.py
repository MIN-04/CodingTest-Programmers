# LEVEL 01 - 12940. 최대공약수와 최소공배수 (https://school.programmers.co.kr/learn/courses/30/lessons/12940)

def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(n, m):
    return [gcd(n,m), lcm(n,m)]
