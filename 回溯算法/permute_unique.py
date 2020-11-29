# -*- coding: utf-8 -*-
"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
示例：
    输入：nums = [1,2,1]
    输出：
    [[1,1,2],
     [1,2,1],
     [2,1,1]]
"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 先对nums排序
        nums = sorted(nums)
        result = []
        arr = []
        visited = set()

        def full_array(k):
            if k == len(nums):
                result.append(arr[:])
                return
            for i, num in enumerate(nums):
                item = (i, num)     # 因为有重复元素，所以访问集合要绑定下标
                if item in visited:
                    continue
                # 剪枝，如果当前元素与前一个元素相同，且前一个元素没有访问过，则跳过
                if i > 0 and num == nums[i-1] and (i-1, nums[i-1]) not in visited:
                    continue
                arr.append(num)
                visited.add(item)
                full_array(k+1)
                visited.remove(item)
                arr.pop()

        full_array(0)
        return result


if __name__ == '__main__':
    nums = [1, 2, 1]
    result = Solution().permuteUnique(nums)
    print(result)