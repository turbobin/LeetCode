# -*- coding: utf-8 -*-
"""
524. 通过删除字母匹配到字典里最长单词
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例：
    输入:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]

    输出: 
    "apple"
"""
class Solution:
    def findLongestWord(self, s, d):
        longest_word = ""
        for ss in d:
            l1 = len(longest_word)
            l2 = len(ss)
            # 如果长度相等，比较字符串的字典序大小
            if l1 > l2 or (l1 == l2 and ss > longest_word):
                continue
            is_substr = self.check_is_substr(s, ss)
            if is_substr:
                longest_word = ss
        return longest_word

    def check_is_substr(self, string, target_str):
        i, j = 0, 0
        while i < len(string) and j < len(target_str):
            if string[i] == target_str[j]:
                j += 1
            i += 1
        return j == len(target_str)


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = "bab"
        d = ["ba","ab","a","b"]
        output = "ab"
        result = self.solution.findLongestWord(s, d)
        self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()