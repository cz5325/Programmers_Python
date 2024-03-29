def solution(s):
    s_list=s.split(" ")
    n = [int(i) for i in s_list]
    n.sort()

    return str(n[0]) + " " + str(n[-1])

