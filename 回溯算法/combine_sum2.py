# -*- coding: utf-8 -*-
"""
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
(链接：https://leetcode-cn.com/problems/combination-sum-ii)

说明：
    - 所有数字（包括目标数）都是正整数。
    - 解集不能包含重复的组合。

示例：
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        arr = []
        visited = set()
        candidates = sorted(candidates)
        n = len(candidates)

        def dfs(target, start=0):
            if target < 0:
                return
            if target == 0:
                result.append(arr[:])

            for i in range(start, n):
                item = (i, candidates[i])
                if item in visited:
                    continue
                # 剪枝，如果当前元素与前一个元素相同，且前一个元素没有访问过，则跳过
                last_item = (i-1, candidates[i-1])
                if (i > 0 and candidates[i] == candidates[i-1]
                        and last_item not in visited):
                    continue
                arr.append(candidates[i])
                visited.add(item)
                num = target - candidates[i]
                dfs(num, i + 1)     # 每个数字只能使用一次，所以这里是i+1 
                visited.remove(item)
                arr.pop()

        dfs(target)
        return result


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    result = Solution().combinationSum2(candidates, target)
    print(result)