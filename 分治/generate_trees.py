# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        result = self._generate_tree(1, n)
        return result

    def _generate_tree(self, start, end):
        if start > end:
            return [None]
        alltrees = []
        for i in range(start, end + 1):
            # i 是根节点
            left_tree = self._generate_tree(start, i -1)
            right_tree = self._generate_tree(i + 1, end)
            for left in left_tree:
                for right in right_tree:
                    tree = TreeNode(i)
                    tree.left = left
                    tree.right = right
                    alltrees.append(tree)
        return alltrees


if __name__ == '__main__':
    n = 3
    result = Solution().generateTrees(n)
    print(result)