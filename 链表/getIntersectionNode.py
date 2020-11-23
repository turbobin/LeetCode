# -*- coding: utf-8 -*-
"""
160. 相交链表
A:          a1 → a2
                    ↘
                      c1 → c2 → c3
                    ↗
B:    b1 → b2 → b3
A，B 两个链表相交于 c1 ，找到这个交点
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node1 = headA
        node2 = headB
        while node1 != node2:   # 注意，当没有交点时，None=None 也满足退出条件
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1