def solution(price, money, count):
    n = 0
    for i in range(1, count+1):
        n += price * i
    result = n - money
    
    return max(0, result)
    
    