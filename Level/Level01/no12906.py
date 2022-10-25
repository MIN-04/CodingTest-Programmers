# LEVEL 01 - 12906. 같은 숫자는 싫어 (https://school.programmers.co.kr/learn/courses/30/lessons/12906)

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            continue
        else: answer.append(arr[i])
    return answer
