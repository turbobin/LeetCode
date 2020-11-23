# -*- coding: utf-8 -*-
"""
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。
(链接：https://leetcode-cn.com/problems/restore-ip-addresses)

示例：
    输入：s = "25525511135"
    输出：["255.255.11.135","255.255.111.35"]
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def dfs(start=0, subarr=[]):
            if len(subarr) == 4 and start == len(s):
                ip = ".".join(subarr)
                result.append(ip)
                return
            elif len(subarr) == 4 and start < len(s):
                return
            elif start > len(s):
                return

            for i in range(1, 4):
                # 以start为起点切成3段
                num = s[start: start+i]
                if len(num) == 3 and int(num) > 255:  # 不能超过255
                    return
                if len(num) > 1 and num[0] == "0":  # 不能有前导0
                    return
                subarr.append(num)
                dfs(start+i, subarr)
                subarr.pop()    # 上面一句的递归分支结束，撤销最后的选择，进入下一轮迭代，考察下一个切割长度

        dfs()
        return result


if __name__ == '__main__':
    s = "25525511135"
    result = Solution().restoreIpAddresses(s)
    print(result)