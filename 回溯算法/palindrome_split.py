# -*- coding: utf-8 -*-
"""
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例：
    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
"""
class Solution:
    def partition(self, s):
        result = []
        arr = []

        def back_track(ss):
            if len(ss) == 0:
                result.append(arr[:])
                return
            for i in range(len(ss)):
                # 判断是否是回文子串
                if not self.is_palindrom(ss[0: i+1]):
                    continue
                arr.append(ss[0: i+1])
                back_track(ss[i+1:])    # # 继续考察右边的子串
                arr.pop()

        back_track(s)
        return result

    def is_palindrom(self, ss):
        i, j = 0, len(ss)-1
        while i < j:
            if ss[i] != ss[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = "aabb"
    result = Solution().partition(s)
    print(result)