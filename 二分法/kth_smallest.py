# -*- coding: utf-8 -*-

class Solution:
    def kthSmallest(self, matrix, k):
        # 使用二分法查找，每次先查找一半，看是否达到了第 k 大元素
        if not matrix or not matrix[0]:
            return None
        n = len(matrix)
        m = len(matrix[0])
        low = matrix[0][0]
        high = matrix[n-1][m-1]
        while low <= high:
            cnt = 0
            mid = low + (high - low) // 2
            i, j = 0, 0
            for i in range(n):
                for j in range(m):
                    if matrix[i][j] > mid:
                        continue
                    cnt += 1
                
            if cnt < k:
                low = mid + 1
        return low


if __name__ == '__main__':
    matrix = [
  [ 1,  5,  9],
  [10, 11, 13],
  [12, 13, 15]
]
    index = Solution().kthSmallest(matrix, 8)
    print(index)