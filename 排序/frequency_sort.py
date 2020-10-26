# -*- coding: utf-8 -*-
"""
451. 根据字符出现频率排序
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例：
    输入:
    "tree"
    输出:
    "eert"

    输入:
    "cccaaa"

    输出:
    "cccaaa"
"""
class Solution(object):
    def frequencySort(self, s):
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        # 字典按value排序
        orderdict = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        ss = ""
        for char, freq in orderdict:
            ss += char * freq
        return ss


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = "cccaaa"
        output = "cccaaa"
        result = self.solution.frequencySort(s)
        self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()