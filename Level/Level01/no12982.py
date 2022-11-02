# LEVEL 01 - 12982. 예산 (https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    cnt = 0
    price = 0
    
    d.sort()
    
    for i in range(len(d)):
        price += d[i]
        
        if price > budget :
            break
        
        cnt += 1
        
    return cnt
