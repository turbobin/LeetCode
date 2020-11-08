# -*- coding: utf-8 -*-
"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
"""
class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
            return
        m = self.min_stack[-1]
        if x < m:
            self.min_stack.append(x)
        else:
            self.min_stack.append(m)

    def pop(self):
        if not self.min_stack:
            return None
        self.min_stack.pop(-1)
        item = self.stack.pop(-1)
        # return item

    def top(self):

        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):

        if not self.min_stack:
            return None
        item = self.min_stack[-1]
        return item


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.getMin())