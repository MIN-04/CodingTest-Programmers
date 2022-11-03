# LEVEL 01 - 42748. K번째수 (https://school.programmers.co.kr/learn/courses/30/lessons/42748)

def solution(array, commands):
    answer = []
    
    for i in commands:
        splitArr = array[i[0] - 1 : i[1]]
        splitArr.sort()
        answer.append(splitArr[i[2]-1])
    
    return answer
