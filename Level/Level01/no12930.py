# LEVEL 01 - 12930. 이상한 문자 만들기 (https://school.programmers.co.kr/learn/courses/30/lessons/12930)

def solution(s):
    arr = s.split(' ')
    answer = ''
    for i in arr:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[:-1]
