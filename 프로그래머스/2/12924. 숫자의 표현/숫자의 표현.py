def solution(n):
    answer = 0
    for i in range(1,n+1):
        total_sum = 0
        for j in range(i, n+1):
            total_sum += j
            if total_sum == n:
                answer+=1
                break
            elif total_sum >n:
                break 
    
    return answer