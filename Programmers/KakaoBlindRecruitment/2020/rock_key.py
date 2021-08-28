# 210829 : 3시간 넘게 삽질
# key에 padding 하여 lock의 모든 홈/돌기를 항상 검사해야 했는데
# locks에 padding 하여 반대로 검사하느라 시간 날
import numpy as np


def solution(key, lock):
    answer = False
    keys = np.array(key)
    locks = np.array(lock)
    N = len(lock)
    M = len(keys)

    # 답이 없는 경우 거르기 : key 돌기 < lock 홈 또는 lock이 전부 돌기일때
    key_dol = sum(sum(keys))
    lock_hom = len(locks) ** 2 - sum(sum(locks))

    if key_dol < lock_hom:
        return False
    if lock_hom == 0:
        return True

    keys = np.pad(keys, (N - 1, N - 1), mode='constant', constant_values=0)

    # 회전시키기
    for r in range(4):
        # 가로, 세로 순으로 움직이며 검사
        for i in range(M + N - 1):
            for j in range(M + N - 1):
                xor = np.logical_xor(keys[i:i + N, j:j + N], locks)

                # 전부 짝이 맞아야 함 True 여야함
                if np.count_nonzero(xor) == N * N:
                    return True

        locks = np.rot90(locks)

    return answer