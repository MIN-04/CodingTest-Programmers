# LEVEL 01 - 12935. 제일 작은 수 제거하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12935)

def solution(arr):
    if arr and arr != [10]:
        idx = arr.index(min(arr))
        arr.pop(idx)
        return arr
    else:
        return [-1]
    
