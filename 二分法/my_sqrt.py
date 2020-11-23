# -*- coding: utf-8 -*-
"""
69. x 的平方根
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
(链接：https://leetcode-cn.com/problems/sqrtx)

示例：
    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842..., 
         由于返回类型是整数，小数部分将被舍去。
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        # 查找最后一个小于等于x的值
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid <= x:
                if mid == x or (mid+1) * (mid+1) > x:
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1
        return None


if __name__ == '__main__':
    result = Solution().mySqrt(8)
    print(result)