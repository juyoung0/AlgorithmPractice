# 210828 : 풀이시간 9qns

def solution(s):
    answer = 1001

    for i in range(1, len(s) + 1):
        prev = s[0:i]
        cnt = 1
        compress = ''
        for j in range(i, len(s), i):
            if s[j:j + i] == prev:
                cnt += 1
            else:
                if cnt == 1:
                    compress += prev
                else:
                    compress += str(cnt) + prev
                prev = s[j:j + i]
                cnt = 1

        if cnt == 1:
            compress += prev
        else:
            compress += str(cnt) + prev

        answer = min(answer, len(compress))
    return answer