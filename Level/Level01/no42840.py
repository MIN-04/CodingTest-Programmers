# LEVEL 01 - 42840. 모의고사 (https://school.programmers.co.kr/learn/courses/30/lessons/42840)

def solution(answers):
    result = []
    
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == std1[idx%5]:
            score[0] += 1
        if answer == std2[idx%8]:
            score[1] += 1
        if answer == std3[idx%10]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)
    
    
    return result
