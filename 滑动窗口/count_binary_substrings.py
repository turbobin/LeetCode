# -*- coding: utf-8 -*-
"""
力扣-696：计数二进制子串。计算具有相同0和1的非空连续子字符串的数量，
如"00110011"，有6个具有相同数量的0和1: "0011", "01", "1100", "10", "0011", "01"
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        n = len(s)
        nums = []
        i = 0
        # 滑动窗口,一头一尾两个指针
        for j in range(n):
            if s[j] != s[i]:
                # 首尾两数不相等时，记录窗口长度，同时使头指针等于尾指针
                nums.append(j-i)
                i = j
            # 边界情况，尾指针到达末尾了
            if j == n - 1:
                nums.append(j-i+1)

        print(nums)     # [2, 1, 2, 2]
        i, j = 0, 1
        result = 0
        while j < len(nums):
            # 相邻两数取最小
            result += min(nums[i], nums[j])
            i += 1
            j += 1
        return result


if __name__ == '__main__':
    s = "0010011"
    result = Solution().countBinarySubstrings(s)
    print(result)