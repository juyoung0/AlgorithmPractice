import sys

if __name__=="__main__":
    nums = list(map(int, input().split()))
    prev = nums[0]
    for n in nums[1:]:
        if abs(n - prev) != 1:
            print("mixed")
            break
        prev = n
    else:
        if nums[0] == 1:
            print("ascending")
        else:
            print("descending")