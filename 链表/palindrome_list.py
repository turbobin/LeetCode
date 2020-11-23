# -*- coding: utf-8 -*-
"""
234. 回文链表
请判断一个链表是否为回文链表。
示例：
    输入: 1->2->2->1
    输出: true
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 先用快慢指针找出中点
        slow = head
        fast = head
        while fast and fast.next:
            slow = head.next
            fast = fast.next.next
        # 从中点开始断开，并翻转后半段
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # 同时从左半段和右半段链表开始判断
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
