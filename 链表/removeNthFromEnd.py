# -*- coding: utf-8 -*-
"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
    给定一个链表: 1->2->3->4->5, 和 n = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # 让一个指针先走n步
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        prev = head
        slow = head
        # 当fast走到末尾时，slow便是倒数第n个节点
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return head

