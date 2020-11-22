# -*- coding: utf-8 -*-
"""
17.电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例：
    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        # 元素下标表示对应的数字键
        keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
        result = []

        def back_track(char, i=0):
            if i == len(digits):
                result.append(char)
                return

            num = int(digits[i])
            letters = keys[num]
            for s in letters:
                back_track(char+s, i+1)

        back_track("")
        return result


if __name__ == '__main__':
    digits = "23"
    result = Solution().letterCombinations(digits)
    print(result)