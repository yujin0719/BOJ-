# level2 : 최댓값과 최솟값

def solution(s):
    answer = ''
    num = list(map(int,s.split(" ")))
    answer += str(min(num))
    answer += " "
    answer += str(max(num))
    return answer
