# -*- coding: utf-8 -*- 
"""
206. 反转链表
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev