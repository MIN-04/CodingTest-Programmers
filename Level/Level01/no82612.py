# LEVEL 01 - 82612. 부족한 금액 계산하기 (https://school.programmers.co.kr/learn/courses/30/lessons/82612)

def solution(price, money, count):
    total = sum(price * N for N in range(1, count + 1))
    return total - money if total > money else 0
        
