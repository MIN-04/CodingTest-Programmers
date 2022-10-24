# LEVEL 01 - 12910. 나누어 떨어지는 숫자 배열 (https://school.programmers.co.kr/learn/courses/30/lessons/12910)

def solution(arr, divisor):
    return sorted(list(i for i in arr if i % divisor == 0)) or [-1]
