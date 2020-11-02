# -*- coding: utf-8 -*-
"""
744. 寻找比目标字母大的最小字母
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。
另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

示例：
    输入:
    letters = ["c", "f", "j"]
    target = "a"
    输出: "c"

    输入:
    letters = ["c", "f", "j"]
    target = "c"
    输出: "f"
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if letters[mid] > target:
                if mid == 0 or letters[mid-1] <= target:
                    return letters[mid]
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return letters[0]


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "a"
    result = Solution().nextGreatestLetter(letters, target)
    print(result)