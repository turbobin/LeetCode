# -*- coding: utf-8 -*-
"""
257. 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def dfs(root, path=[]):
            if not root:
                return
            if not root.left and not root.right:
                path.append(str(root.val))  # 叶子节点
                result.append("->".join(path))
                return
            path.append(str(root.val))
            if root.left:
                dfs(root.left, path)
                path.pop()  # 退出栈时需要清掉入栈的数据
            if root.right:
                dfs(root.right, path)
                path.pop()

        dfs(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    result = Solution().binaryTreePaths(root)
    print(result)