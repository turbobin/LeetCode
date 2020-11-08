# -*- coding: utf-8 -*-
"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例：
输入: 1->1->2->3->3
输出: 1->2->3
"""

class Solution(object):
    def deleteDuplicates(self, head):
        prev = head
        curr = head
        while curr and curr.next:
            curr = curr.next
            if curr.val == prev.val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head