# -*- coding: utf-8 -*-
"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
1.初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
2.你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例：
    输入：
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    输出：[1,2,2,3,5,6]
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """归并排序的思想"""
        tmp = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
        # 判断哪个数组中还有元素
        start = j if i == m else i
        remain_arr = nums2[start: n] if i == m else nums1[start: m]
        tmp += remain_arr
        # 把tmp数组拷贝到 nums1
        for k in range(m+n):
            nums1[k] = tmp[k]

    def merge2(self, nums1, m, nums2, n):
        """
        解法2：倒序比较数组元素，将最大值放到数组末尾，
        这样才不会把前面排序好的元素覆盖
        """
        i, j = m-1, n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # 把剩余nums2数组拷贝到nums1中
        if i < 0:
            for index in range(j+1):
                nums1[index] = nums2[index]


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums1 = [1,0,0,0,0]
        m = 1
        nums2 = [2,5,6]
        n = 3
        output = [1,2,5,6,0]
        self.solution.merge2(nums1, m, nums2, n)
        self.assertEqual(output, nums1)


if __name__ == '__main__':
    unittest.main()