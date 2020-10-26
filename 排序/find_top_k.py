# -*- coding: utf-8 -*-
"""
215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例：
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        维护一个k大小的小顶堆，最后堆顶的元素就是第k大元素
        """
        import queue
        q = queue.PriorityQueue()
        for num in nums:
            q.put(num)
            if q.qsize() > k:
                q.get()     # 删除堆顶元素
        return q.get()


import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        output = 4
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()