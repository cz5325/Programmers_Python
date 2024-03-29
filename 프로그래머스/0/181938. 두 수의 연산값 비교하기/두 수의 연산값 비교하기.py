def solution(a, b):
    
    sum = int(str(a) + str(b))
    product = 2 * a * b
    if sum >= product:
        return sum
    else:
        return product
    