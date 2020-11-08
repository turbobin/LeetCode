# -*- coding: utf-8 -*-
"""
445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。
数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
(链接：https://leetcode-cn.com/problems/add-two-numbers-ii)
要求：输入的链表不能修改，即不能对链表进行翻转
示例：
    输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 8 -> 0 -> 7
    解释：7243 + 564 = 7807
"""
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 由于计算和需要先链表末尾数相加，但是不能翻转链表，所以先遍历两个链表，使用栈来存储值
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        l = ListNode()
        head = l
        c = 0   # c表示余数
        while stack1 or stack2 or c:    # 如果两个栈空了，还要判断下余数是否为0
            a = stack1.pop(-1) if stack1 else 0
            b = stack2.pop(-1) if stack2 else 0
            item = a + b + c
            c, val = divmod(item, 10)
            node = ListNode(val)
            node.next = head.next
            head.next = node
        return head.next
