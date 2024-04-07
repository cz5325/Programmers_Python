def solution(phone_number):
    back_number = phone_number[-4:] 
    star = "*" * (len(phone_number) - 4) 
    return f"{star}{back_number}"