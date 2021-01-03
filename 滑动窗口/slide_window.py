# -*- coding: utf-8 -*-

def find_max_count(nums):
    prev = None
    max_cnt = 0
    cnt = 0
    arr = []
    for num in nums:
        if num != prev:
            cnt = 0
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            arr = []
            arr.append(num)
        elif cnt == max_cnt:
            arr.append(num)
        prev = num

    print(arr)
    return arr


def slide_window(nums):
    n = len(nums)
    i = 0
    max_cnt = 0
    cnt = 0
    arr = []
    for j in range(n):
        cnt += 1
        if nums[j] != nums[i]:
            cnt = 1
            i = j
        if cnt > max_cnt:
            max_cnt = cnt
            arr = []
            arr.append(nums[j])
        elif cnt == max_cnt:
            arr.append(nums[j])

    print(arr)
    return arr


if __name__ == "__main__":
    nums = [1,2,2,3,3,4,4]
    find_max_count(nums)
    slide_window(nums)