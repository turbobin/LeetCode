# -*- coding: utf-8 -*-
"""
725. 分隔链表
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
(链接：https://leetcode-cn.com/problems/split-linked-list-in-parts)
示例：
    输入: root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
    输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    解释: 输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # 先计算整个链表的长度
        N = 0
        head = root
        while head:
            N += 1
            head = head.next
        # 计算可以分割的长度和余数
        length, mod = divmod(N, k)
        result = []
        for i in range(k):
            # 每段的限制长度，把余数平均分配给前面分割的平均长度
            limit = length + 1 if mod > 0 else length
            mod -= 1
            node = ListNode()
            curr = node
            n = 0
            while root:
                curr.next = root
                curr = curr.next
                root = root.next
                n += 1
                # 当达到限制长度的时候，最后一个指针指向None，并退出循环
                if n == limit:
                    curr.next = None
                    break
            result.append(node.next)
        return result





