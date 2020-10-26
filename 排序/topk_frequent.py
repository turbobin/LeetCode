# -*- coding: utf-8 -*-
"""
347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例：
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

    输入: nums = [1], k = 1
    输出: [1]
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        # 先统计每个元素的频率
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        from queue import PriorityQueue
        # 使用最小堆存储前k大频率最高的元素
        q = PriorityQueue()
        for key, value in hashmap.items():
            item = (value, key)
            q.put(item)
            if q.qsize() > k:
                q.get()
        arr = [None] * k
        while not q.empty():
            freq, num = q.get()
            arr[k-1] = num
            k -= 1
        return arr

    def topKFrequent2(self, nums, k):
        """思路2：桶排序"""
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        # 相同元素散落到同一个桶内，桶下标为元素出现的次数
        bucket = [None] * len(nums)
        for key, value in hashmap.items():
            bucket[value] = key
        arr = []
        i = 0
        for item in bucket[::-1]:
            if item == None:
                continue
            i += 1
            if i <= k:
                arr.append(item)
        return arr





import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [1,1,1,2,2,3]
        k = 2
        output = [1, 2]
        result = self.solution.topKFrequent2(nums, k)
        self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()

