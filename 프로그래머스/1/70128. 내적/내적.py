def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i] 
    return answer
    
    
    # a와 b를 인덱스별로 곱한 후 더한값