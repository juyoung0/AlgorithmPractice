# list slicing 하는 부분에서 시간초과나서 주석처리하고 수정하여 통과함

import sys

def find_idx(arr, elem):
    left, right = 0, len(arr)
    mid = (left + right) // 2
    while left < right:
        if arr[mid] < elem:
            left = mid + 1
        elif arr[mid] > elem:
            right = mid
        else:
            break
        mid = (left + right) // 2

    if mid >= len(arr):
        arr.append(elem)
    else:
        arr[mid] = elem
    result = arr
    # result = arr[:mid] + [elem] + arr[mid+1:]
    return (result, mid)


if __name__ == "__main__":
    n = int(input())
    stone = list(map(int, sys.stdin.readline().split()))
    sort_l = []
    sort_r = []
    step_l = [0 for _ in range(n)]
    step_r = [0 for _ in range(n)]
    for i in range(0, n):
        sort_l, idx_l = find_idx(sort_l, stone[i])
        step_l[i] = idx_l + 1

        sort_r, idx_r = find_idx(sort_r, stone[n - i - 1])
        step_r[n - i - 1] = idx_r + 1

    result = [l + r for l, r in zip(step_r, step_l)]
    print(max(result) - 1)