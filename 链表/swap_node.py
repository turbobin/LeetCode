# -*- coding: utf-8 -*-
"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
示例：
输入：head = [1,2,3,4]
输出：[2,1,4,3]
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        # 先建一个前驱节点指向头元素
        l = ListNode()
        pprev = l
        pprev.next = head
        prev = head
        curr = head.next
        while curr:
            # 断开第二个节点，和前一个元素交换
            prev.next = curr.next
            curr.next = prev
            pprev.next = curr

            pprev = prev
            prev = prev.next
            if prev:
                curr = prev.next
            else:
                break
        return l.next