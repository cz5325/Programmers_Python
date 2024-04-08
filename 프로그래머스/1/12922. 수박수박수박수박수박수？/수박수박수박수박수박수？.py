def solution(n):
    watermellon = ''
    
    for i in range(n):
        if i % 2 == 0:
            watermellon += '수'
        else:
            watermellon += '박'
    
    return watermellon
                