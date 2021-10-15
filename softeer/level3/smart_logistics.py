n, k = map(int, input().split())
line = list(input())
cnt = 0
for i in range(n):
    if line[i] == 'P':
        # 앞에 있는 물건 먼저 집기
        for j in range(k, 0, -1):
            if i-j >= 0 and line[i-j] == 'H':
                line[i-j] = 'E'
                line[i] = 'Q'
                cnt += 1
                break
        else:
            # 못잡았을 경우 뒤에 있는 물건 집기
            for j in range(1, k+1):
                if i+j >= n:
                    break
                if line[i+j] == 'H':
                    line[i+j] = 'E'
                    line[i] = 'Q'
                    cnt += 1
                    break

print(cnt)