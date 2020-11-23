# -*- coding: utf-8 -*-
"""
739. 每日温度
找出数组中元素与下一个比它大的元素之间的距离，如果数组中没有比它高的元素，输出0
如：
给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
（链接：https://leetcode-cn.com/problems/daily-temperatures）
"""

class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        arr = [0] * n
        # 用一个栈来保存当前还没有找到比它大的元素
        stack = []
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                prev = stack.pop(-1)
                arr[prev] = i - prev
            stack.append(i)     # 保存对应元素下标
        return arr


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = Solution().dailyTemperatures(temperatures)
    print(result)

