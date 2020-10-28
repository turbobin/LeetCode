# -*- coding: utf-8 -*-
"""
241. 为运算表达式设计优先级
给表达式加括号，输出不同的结果（链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses）

示例:
    输入: "2-1-1"
    输出: [0, 2]
    解释: 
    ((2-1)-1) = 0 
    (2-(1-1)) = 2

    输入: "2*3-4*5"
    输出: [-34, -14, -10, -10, 10]
    解释: 
    (2*(3-(4*5))) = -34 
    ((2*3)-(4*5)) = -14 
    ((2*(3-4))*5) = -10 
    (2*((3-4)*5)) = -10 
    (((2*3)-4)*5) = 10
"""

class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i, ch in enumerate(input):
            if ch in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                print left, right, ch
                for l in left:
                    for r in right:
                        if ch == "+":
                            res.append(l + r)
                        elif ch == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res
    

if __name__ == '__main__':
    input = "2*3-4*5"
    output = Solution().diffWaysToCompute(input)
    print(output)