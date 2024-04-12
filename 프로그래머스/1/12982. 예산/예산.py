def solution(d, budget):
    cnt = 0  # 지원 가능한 부서의 개수 초기화
    d.sort()  # 신청 금액을 오름차순으로 정렬

    for i in d:
        if budget < i:
            break
        budget -= i
        cnt += 1

    return cnt

