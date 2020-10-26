# -*- coding: utf-8 -*-

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif n <= 2:
            return n
        queue = [(0, 0, 1)]
        grid[0][0] = 1
        while queue:
            i, j, step = queue.pop(0)
            print("queue:", queue)
            # print(i, j, step)
            for dx, dy in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
                if i+dx == n-1 and j+dy == n-1:
                    return step + 1
                if 0 <= i+dx < n and 0 <= j+dy < n and grid[i+dx][j+dy] == 0:
                    print(i+dx, j+dy)
                    queue.append((i+dx, j+dy, step+1))
                    grid[i+dx][j+dy] = 1  # mark as visited                   
        return -1


if __name__ == '__main__':
    s = Solution()
    grid = [[0,0,0],[1,0,0],[1,1,0]]
    path = s.shortestPathBinaryMatrix(grid)
    print(path)