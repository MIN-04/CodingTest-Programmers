# 분수의 덧셈

import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    resultGcd = math.gcd(denum, num)
    return [denum // resultGcd, num // resultGcd]
