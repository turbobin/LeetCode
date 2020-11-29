# -*- coding: utf-8 -*-
"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
(链接：https://leetcode-cn.com/problems/combination-sum)

说明：
    - 所有数字（包括 target）都是正整数。
    - 解集不能包含重复的组合。 

示例：
    输入：candidates = [2,3,6,7], target = 7,
    所求解集为：
    [
      [7],
      [2,2,3]
    ]
"""

class Solution:
    def combinationSum(self, candidates, target):
        result = []
        arr = []
        n = len(candidates)

        def dfs(target, start=0):
            if target < 0:
                return
            if target == 0:
                result.append(arr[:])
                return

            for i in range(start, n):
                arr.append(candidates[i])
                num = target - candidates[i]    # 用户目标值减去数组中的元素作为新的目标值
                dfs(num, i)     # 元素可以无限制取，所以这里是i，而不是i+1
                arr.pop()

        dfs(target)
        return result


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    result = Solution().combinationSum(candidates, target)
    print(result)