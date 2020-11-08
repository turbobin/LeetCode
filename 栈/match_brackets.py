# -*- coding: utf-8 -*-
"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
 1.左括号必须用相同类型的右括号闭合。
 2.左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""
class Solution(object):
    def isValid(self, s):
        stack = []
        match = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in match:
                stack.append(c)
            if not stack:
                return False
            if c not in match and c != match[stack.pop(-1)]:
                return False
        # 最后要检查栈是否空了
        return True if not stack else False


if __name__ == '__main__':
    s = "()[]{}"
    result = Solution().isValid(s)
    print(result)