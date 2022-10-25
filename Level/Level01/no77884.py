# LEVEL 01 - 77884. 약수의 개수와 덧셈 (https://school.programmers.co.kr/learn/courses/30/lessons/77884)

# 방법 1.
def solution(left, right):
    sum = 0
    for i in range(left, right + 1):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div % 2 == 0:
            sum += i
        else: sum -= i
    return sum

# 방법 2. (속도가 훨씬 적게 걸린다.)
def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            sum -= i
        else:
            sum += i
    return 
