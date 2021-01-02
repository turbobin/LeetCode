# LeetCode 题解

[数组与矩阵](#数组与矩阵)
 * [把数组中的 0 移到末尾](#把数组中的-0-移到末尾)
 * [重塑矩阵](#重塑矩阵)
 * [找出数组中最长的连续 1 个数](#找出数组中最长的连续-1-个数)
 * [有序矩阵查找目标值](#有序矩阵查找目标值)
 * [有序矩阵的 Kth Element](#有序矩阵的-kth-element)
 * [一个数组元素在 [1, n] 之间，其中一个数被替换为另一个数，找出重复的数和丢失的数](#一个数组元素在-1-n-之间其中一个数被替换为另一个数找出重复的数和丢失的数)
 * [找出数组中重复的数，数组值在 [1, n] 之间](#找出数组中重复的数数组值在-1-n-之间)
 * [数组的度](#数组的度)
 * [对角元素相等的矩阵](#对角元素相等的矩阵)
 * [嵌套数组](#嵌套数组)
 * [分隔数组](#分隔数组)

[链表](#链表)

 * [找出两个链表的交点](#找出两个链表的交点)
 * [链表反转](#链表反转)
 * [归并两个有序的链表](#归并两个有序的链表)
 * [从有序链表中删除重复节点](#从有序链表中删除重复节点)
 * [删除链表的倒数第 n 个节点](#删除链表的倒数第-n-个节点)
 * [交换链表中的相邻结点](#交换链表中的相邻结点)
 * [链表求和](#链表求和)
 * [回文链表](#回文链表)
 * [固定分隔链表](#固定分隔链表)
 * [链表元素按奇偶重排](#链表元素按奇偶重排)

[栈和队列](#栈和队列)
 * [用栈实现队列](#用栈实现队列)
 * [用队列实现栈](#用队列实现栈)
 * [最小值栈](#最小值栈)
 * [用栈实现括号匹配](#用栈实现括号匹配)
 * [数组中元素与下一个比它大的元素之间的距离](#数组中元素与下一个比它大的元素之间的距离)
 * [循环数组中比当前元素大的下一个元素](#循环数组中比当前元素大的下一个元素)

[哈希表](#哈希表)
 * [两数之和](#两数之和)
 * [判断数组是否含有重复元素](#判断数组是否含有重复元素)
 * [最长和谐序列](#最长和谐序列)
 * [最长连续序列](#最长连续序列)

[字符串](#字符串)
 * [两个字符串包含的字符是否完全相同](#两个字符串包含的字符是否完全相同)
 * [计算一组字符集合可以组成的回文字符串的最大长度](#计算一组字符集合可以组成的回文字符串的最大长度)
 * [字符串同构](#字符串同构)
 * [回文子字符串个数](#回文子字符串个数)
 * [判断一个整数是否是回文数](#判断一个整数是否是回文数)
 * [统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数](#统计二进制字符串中连续-1-和连续-0-数量相同的子字符串个数)

[树](#树)
 * [树的高度](#树的高度)
 * [平衡树](#平衡树)
 * [两节点的最长路径](#两节点的最长路径)
 * [翻转二叉树](#翻转二叉树)
 * [合并两棵树](#合并两棵树)
 * [判断路径和是否等于一个数](#判断路径和是否等于一个数)
 * [统计路径和等于一个数的路径数量](#统计路径和等于一个数的路径数量)
 * [子树](#子树)
 * [树的对称](#树的对称)
 * [二叉树最小深度](#二叉树最小深度)
 * [统计左叶子节点的和](#统计左叶子节点的和)
 * [相同节点值的最大路径长度](#相同节点值的最大路径长度)
 * [间隔遍历](#间隔遍历)
 * [找出二叉树中第二小的节点](#找出二叉树中第二小的节点)
 * [一棵树每层节点的平均数](#一棵树每层节点的平均数)
 * [得到左下角的叶子节点](#得到左下角的叶子节点)
 * [非递归实现二叉树的前序遍历](#非递归实现二叉树的前序遍历)
 * [非递归实现二叉树的后序遍历](#非递归实现二叉树的后序遍历)
 * [非递归实现二叉树的中序遍历](#非递归实现二叉树的中序遍历)
 * [修剪二叉查找树](#修剪二叉查找树)
 * [寻找二叉查找树的第 k 个元素](#寻找二叉查找树的第-k-个元素)
 * [把二叉查找树每个节点的值都加上比它大的节点的值](#把二叉查找树每个节点的值都加上比它大的节点的值)
 * [二叉查找树的最近公共祖先](#二叉查找树的最近公共祖先)
 * [二叉树的最近公共祖先](#二叉树的最近公共祖先)
 * [从有序数组中构造二叉查找树](#从有序数组中构造二叉查找树)
 * [根据有序链表构造平衡的二叉查找树](#根据有序链表构造平衡的二叉查找树)
 * [在二叉查找树中寻找两个节点，使它们的和为一个给定值](#在二叉查找树中寻找两个节点使它们的和为一个给定值)
 * [在二叉查找树中查找两个节点之差的最小绝对值](#在二叉查找树中查找两个节点之差的最小绝对值)
 * [寻找二叉查找树中出现次数最多的值](#寻找二叉查找树中出现次数最多的值)
 * [实现一个 Trie](#实现一个-trie)
 * [实现一个 Trie，用来求前缀和](#实现一个-trie用来求前缀和)

[双指针](#双指针)
 * [有序数组的 Two Sum](#有序数组的-two-sum)
 * [两数平方和](#两数平方和)
 * [反转字符串中的元音字符](#反转字符串中的元音字符)
 * [回文字符串](#回文字符串)
 * [归并两个有序数组](#归并两个有序数组)
 * [判断链表是否存在环](#判断链表是否存在环)
 * [最长子序列](#最长子序列)

[排序](#排序)

 * [出现频率最多的 k 个元素](#出现频率最多的-k-个元素)
 * [按照字符出现次数对字符串排序](#按照字符出现次数对字符串排序)
 * [荷兰国旗问题(按颜色排序)](#荷兰国旗问题按颜色排序)

[二分查找](#二分查找)

 * [求开方](#求开方)
 * [找出大于给定元素的最小元素](#找出大于给定元素的最小元素)
 * [找出有序数组的单个元素](#找出有序数组的单个元素)
 * [第一个错误的版本](#第一个错误的版本)
 * [旋转数组的最小数字](#旋转数组的最小数字)
 * [有序数组中连续出现数字的区间](#有序数组中连续出现数字的区间)

[分治](#分治)
 * [给表达式加括号求值](#给表达式加括号求值)
 * [不同的二叉搜索树 II](#不同的二叉搜索树-ii)

[广度优先搜索(BFS)](#广度优先搜索bfs)
 * [计算在网格中从原点到特定点的最短路径长度](#计算在网格中从原点到特定点的最短路径长度)
 * [组成整数的最小平方数数量](#组成整数的最小平方数数量)
 * [最短单词路径](#最短单词路径)

[深度优先搜索(DFS)](#深度优先搜索dfs)
 * [岛屿的最大面积](#岛屿的最大面积)
 * [岛屿的数量](#岛屿的数量)
 * [朋友圈数量](#朋友圈数量)
 * [填充被围绕的区域](#填充被围绕的区域)
 * [能到达的太平洋和大西洋的区域](#能到达的太平洋和大西洋的区域)

[回溯算法](#回溯算法)
 * [数字键盘组合](#数字键盘组合)
 * [IP 地址划分](#ip-地址划分)
 * [在矩阵中查找字符串](#在矩阵中查找字符串)
 * [输出二叉树中所有从根到叶子的路径](#输出二叉树中所有从根到叶子的路径)
 * [不含重复元素的全排列](#不含重复元素的全排列)
 * [含有相同元素的全排列](#含有相同元素的全排列)
 * [组合问题](#组合问题)
 * [不含相同元素的组合求和](#不含相同元素的组合求和)
 * [含有相同元素的组合求和](#含有相同元素的组合求和)
 * [1-9 数字的组合求和](#1-9-数字的组合求和)
 * [不含相同元素求子集](#不含相同元素求子集)
 * [含有相同元素求子集](#含有相同元素求子集)
 * [分割字符串使得每个部分都是回文数](#分割字符串使得每个部分都是回文数)
 * [N 皇后问题](#n-皇后问题)

[贪心算法](#贪心算法)
 * [分配饼干](#分配饼干)
 * [不重叠的区间个数](#不重叠的区间个数)
 * [投飞镖刺破气球](#投飞镖刺破气球)
 * [根据身高和序号重组队列](#根据身高和序号重组队列)
 * [买卖股票最大的收益](#买卖股票最大的收益)
 * [买卖股票的最大收益 II](#买卖股票的最大收益-ii)
 * [种植花朵](#种植花朵)
 * [判断是否为子序列](#判断是否为子序列)
 * [修改一个数成为非递减数组](#修改一个数成为非递减数组)
 * [子数组最大的和](#子数组最大的和)
 * [分隔字符串使同种字符出现在一起](#分隔字符串使同种字符出现在一起)

[动态规划](#动态规划)

 * [斐波那契数列](#斐波那契数列)
    * [爬楼梯问题](#爬楼梯问题)
    * [强盗抢劫](#强盗抢劫)
    * [强盗在环形街区抢劫](#强盗在环形街区抢劫)
 * [矩阵路径](#矩阵路径)
    * [矩阵的最小路径和](#矩阵的最小路径和)
    * [矩阵的总路径数](#矩阵的总路径数)
 * [数组区间](#数组区间)
    * [数组区间和](#数组区间和)
    * [数组中等差递增子区间的个数](#数组中等差递增子区间的个数)
 * [分割整数](#分割整数)
    * [分割整数的最大乘积](#分割整数的最大乘积)
    * [按平方数来分割整数](#按平方数来分割整数)
    * [分割整数构成字母字符串](#分割整数构成字母字符串)
 * [最长子序列](#最长子序列-1)
    * [最长递增子序列](#最长递增子序列)
    * [一组整数对能够构成的最长链](#一组整数对能够构成的最长链)
    * [最长摆动子序列](#最长摆动子序列)
    * [最长公共子序列](#最长公共子序列)
 * [0-1 背包问题](#0-1-背包问题)
    * [划分数组为和相等的两部分](#划分数组为和相等的两部分)
    * [改变一组数的正负号使得它们的和为一给定数](#改变一组数的正负号使得它们的和为一给定数)
    * [01 字符构成最多的字符串](#01-字符构成最多的字符串)
    * [找零钱的最少硬币数](#找零钱的最少硬币数)
    * [找零钱的硬币数组合](#找零钱的硬币数组合)
    * [字符串按单词列表分割](#字符串按单词列表分割)
    * [组合总和](#组合总和)
 * [股票交易](#股票交易)
    * [需要冷却期的股票交易](#需要冷却期的股票交易)
    * [需要交易费用的股票交易](#需要交易费用的股票交易)
    * [只能进行两次的股票交易](#只能进行两次的股票交易)
    * [只能进行 k 次的股票交易](#只能进行-k-次的股票交易)
 * [字符串编辑](#字符串编辑)
    * [删除两个字符串的字符使它们相等](#删除两个字符串的字符使它们相等)
    * [编辑距离](#编辑距离)
    * [复制粘贴字符](#复制粘贴字符)


## 数组与矩阵

### 把数组中的 0 移到末尾

[力扣-283](https://leetcode-cn.com/problems/move-zeroes/description/)

![image-20201213110155042](https://gitee.com/turbobin_cao/images/raw/master/image-20201213110155042.png)

**解题思路**：

**方法一：** 首先想到的是可以利用冒泡的思想，将等于 0 的元素依次挪到最后。这里有个优化，每次都判断下是否有元素交换，如果没有交换则可以直接退出循环。冒泡的时间复杂度为 O(n<sup>2</sup>)。

```python
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n-1):
            swap = False
            for j in range(n-i-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if not swap:
                break
        return nums
```

**方法二：** 利用指针，先把不等于 0 的元素往前挪，剩余的数字全部赋值 0。时间复杂度接近 O(n)。

```python
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        n = len(nums)
        while i < n:
            nums[i] = 0
            i += 1
        return nums
```

### 重塑矩阵

[力扣-566](https://leetcode-cn.com/problems/reshape-the-matrix/description/)

![image-20201213112457704](https://gitee.com/turbobin_cao/images/raw/master/image-20201213112457704.png)

**解题思路：** 如果要重塑一个矩阵，那么前后元素总数必须是相同的，并且(行数 * 列数) 的积必须相等，此外遍历元素的时候还要注意列元素满了要换行，具体看如下代码。

```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        if not nums:
            return nums
        n = len(nums)
        m = len(nums[0])
        if n * m != r * c:
            return nums
        reshape_nums = []
        arr = []
        k = 0	# 记录遍历到第几个元素了
        for i in range(n):
            for j in range(m):
                num = nums[i][j]
                arr.append(num)
                k += 1
                if k % c == 0:	# 列满了，换行
                    reshape_nums.append(arr)
                    arr = []	# 注意重置为空
        return reshape_nums
```

### 找出数组中最长的连续 1 个数

[力扣-485](https://leetcode-cn.com/problems/max-consecutive-ones/description/)

![image-20201213115002682](https://gitee.com/turbobin_cao/images/raw/master/image-20201213115002682.png)

**解题思路：** 这题一不小心就想复杂了，其实就是简单的计数，然后比较最大值

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        MAX = 0
        for num in nums:
            cnt = cnt + 1 if num == 1 else 0
            if cnt > MAX:
                MAX = cnt       
        return MAX
```

### 有序矩阵查找目标值

[力扣-240](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/)

![image-20201213124047137](https://gitee.com/turbobin_cao/images/raw/master/image-20201213124047137.png)

**解题思路：**

**方法一：** 搜索算法，一般想到广度优先搜索(BFS)或深度优先搜索(DFS)。该选哪一种呢？如果是 BFS，起点的选择很重要，如果直接从左上角搜索到右下角，最坏情况复杂度较高，将导致超时，合适的起点位置应该是右上角或左下角，并在搜索过程中不断调整搜索方向；如果选择 DFS，则建议选择中间位置开始搜索，如果比目标值小，则往右下角搜索，否则往左上角搜索。

**BFS 解题代码**：

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m = len(matrix[0])
        visited = set()
        start = (0, m-1)
        queue = [start]
        
        def bfs():
            while queue:
                item = queue.pop(0)
                if item in visited:
                    continue
                visited.add(item)
                i, j = item
                if i < 0 or j < 0 or i >= n or j >= m:
                    continue
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    queue.append((i-1, j))
                    queue.append((i, j-1))
                else:
                    queue.append((i+1, j))
                    queue.append((i, j+1))
            return False

        return bfs()
```

**DFS 解题代码：**

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m = len(matrix[0])
        visited = set()
        self.find = False
        
        def dfs(i, j):
            if self.find:
                return
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            item = (i, j)
            if item in visited:
                return
            visited.add(item)
            if matrix[i][j] == target:
                self.find = True
            elif matrix[i][j] < target:	# 往左上角方向搜索
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i+1, j+1)
            else:	# 往右下角方向搜索
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i-1, j-1)

        dfs(n >> 1, m >> 1)     # 从中间位置开始查找
        return self.find
```

**方法二：** 因为这是一个有序矩阵，可以使用类似二分查找的算法。起点同样选择从右上角开始搜索。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or matrix[0] == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = m - 1
        while low < n and high >= 0:
            if matrix[low][high] == target:
                return True
            elif matrix[low][high] > target:
                high -= 1
            else:
                low += 1
        return False
```

### 有序矩阵的 Kth Element

[力扣-378](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/)

![image-20201213152703882](https://gitee.com/turbobin_cao/images/raw/master/image-20201213152703882.png)

**解题思路：**

**方法一：** 求 top k 或者求第 k 大、第 k 小元素，一般采用堆来求解。第 k 大元素使用小顶堆，第 k 小元素则使用大顶堆。编程语言中一般实现的是优先级队列，这是一个小顶堆结构，而求解第 k 小元素可以转化为求第 `n-k+1` 大元素。

```python
import Queue
class Solution(object):
    def kthSmallest(self, matrix, k):
        if not matrix or not matrix[0]:
            return None
        n = len(matrix)
        m = len(matrix[0])
        # 维护一个小顶堆，第 k 小的元素就是第 n*m-k+1 大元素
        queue = Queue.PriorityQueue()
        for i in range(n):
            for j in range(m):
                item = matrix[i][j]
                queue.put(item)
                if queue.qsize() > (n * m - k + 1):
                    queue.get()
        return queue.get()
```

**方法二：** 由于这是一个升序排序的数组，可以使用二分查找，每次先查找一半，看是否达到了第 k 大元素。

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        if not matrix or not matrix[0]:
            return None
        n = len(matrix)
        m = len(matrix[0])
        low = matrix[0][0]
        high = matrix[n-1][m-1]
        while low <= high:
            cnt = 0
            mid = low + (high - low) // 2
            for i in range(n):
                # 每次需要遍历完全部元素才能判断，因为下一层有可能有相等的元素
                for j in range(m):
                    if matrix[i][j] > mid:
                        break
                    cnt += 1
            if cnt < k:
                low = mid + 1
            else:
                high = mid - 1
        return low
```

### 一个数组元素在 [1, n] 之间，其中一个数被替换为另一个数，找出重复的数和丢失的数

[力扣-645](https://leetcode-cn.com/problems/set-mismatch/description/)

![image-20201213162145996](https://gitee.com/turbobin_cao/images/raw/master/image-20201213162145996.png)

**解题思路：**

**方法一：** 利用 bitmap 的思想，申请一个长度为 n+1 的数组，存放 1~n 的整数，从下标 1 开始遍历，值为 0 的则为缺失的元素，值为 2 的则为重复的元素。

```python
class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        bitmap = [0] * (n + 1)
        for num in nums:
            bitmap[num] = bitmap[num] + 1
        result = [-1, -1]
        for i in range(1, n+1):
            if bitmap[i] == 0:
                result[1] = i
            if bitmap[i] == 2:
                result[0] = i
        return result
```

**方法二：** 通过交换元素的方式使得数组下标与元素对齐，最后遍历找出未对齐的元素和下标即为所求。

```python
class Solution(object):
    def findErrorNums(self, nums):
        nums = [0] + nums
        n = len(nums)
        i = 0
        while i < n:
            j = nums[i]
            if nums[i] != i and nums[j] != j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for k, num in enumerate(nums):
            if k != num:
                return [num, k]
        return None
```

### 找出数组中重复的数，数组值在 [1, n] 之间

[力扣-287](https://leetcode-cn.com/problems/find-the-duplicate-number/description/)

![image-20201213174217007](https://gitee.com/turbobin_cao/images/raw/master/image-20201213174217007.png)

> 要求：不能使用额外的空间，不能更改原数组。

**解题思路：** 按本题的要求：不能使用额外空间，也不能更改原数组，也就是不能使用 bitmap 解法，也不能通过交换元素的方式来求解。那么只有使用双指针了，但是这是一个无序数组，也不能按常规的双指针解法。解题方法还是比较难想到，由于这是一个 1~n 范围的数组，只有一个重复的元素，可以根据元素值**跳转到对应的下标**来访问元素，由于存在重复的元素，访问的路径最后会构成一个环，如 [1,3,4,2,2] 的访问，访问的元素为 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 ......，题目变成了求解环的入口，可以使用快慢指针来求解。

```python
class Solution(object):
    def findDuplicate(self, nums):
        # 快慢指针必须初始化为一前一后，不能在同一个位置
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            # slow 走一步，fast 走两步
            slow =  nums[slow]
            fast = nums[nums[fast]]

        # slow 放到起点，这时候 slow 和 fast 每次都走一步，直到两个再次相遇
        slow = 0
        while slow != fast:
            # 两个点再次相遇时，即是环的入口
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
```

### 数组的度

[力扣-697](https://leetcode-cn.com/problems/degree-of-an-array/description/)

![image-20201214001432297](https://gitee.com/turbobin_cao/images/raw/master/image-20201214001432297.png)

**解题思路：** 首先要求出数组的度，即求出每个元素出现的次数的最大值，还要求出拥有相同度的最短连续子数组，其实就是求相同元素第一次出现的下标和最后一次出现的下标，两个下标之差就是连续子数组的长度。

```python
class Solution(object):
    def findShortestSubArray(self, nums):
        # 使用hashmap存储每个元素出现的下标
        hashmap = {}
        degree = 0
        for i, num in enumerate(nums):
            if num in hashmap:
                hashmap[num].append(i)
            else:
                hashmap[num] = [i]
            degree = max(degree, len(hashmap[num]))
            
        min_len = float("inf")
        for value in hashmap.values():
            if len(value) != degree:
                continue
            # 求出相同元素第一次和最后一次出现的距离
            length = value[-1] - value[0] + 1
            min_len = min(min_len, length)
        return min_len
```

### 对角元素相等的矩阵

[力扣-766](https://leetcode-cn.com/problems/toeplitz-matrix/description/)

![image-20201214002800339](https://gitee.com/turbobin_cao/images/raw/master/image-20201214002800339.png)

**解题思路：** 遍历元素，判断 `matrix[i][j]` 与 `matrix[i+1][j+1]` 是否相等。注意边界条件的判断。

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n-1):
            for j in range(m-1):
                if i >= n or j >= m:
                    continue
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
```

### 嵌套数组

[力扣-565](https://leetcode-cn.com/problems/array-nesting/description/)

![image-20201214005933539](https://gitee.com/turbobin_cao/images/raw/master/image-20201214005933539.png)

**解题思路：** 不断根据元素的值跳到对应下标，为防止出现访问路径变成环，需要对访问过的位置进行标记，同时记录访问路径的长度，最后求出长度的最大值。

```python
class Solution(object):
    def arrayNesting(self, nums):
        n = len(nums)
        MAX = 0
        for i in range(n):
            cnt = 0
            j = i
            while nums[j] != -1:
                j = nums[j]
                nums[i] = -1
                cnt += 1
            MAX = max(MAX, cnt)
        return MAX
```

### 分隔数组

[力扣-769](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/description/)

![image-20201214011552296](https://gitee.com/turbobin_cao/images/raw/master/image-20201214011552296.png)

**解题思路：** 转化为求有多少个元素可以与下标对齐，相邻元素可以交换。

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        if not arr:
            return 0
        n = len(arr)
        cnt = 0
        num = arr[0]
        for j in range(n):
            num = max(arr[j], num)
            if num == j:
                cnt += 1
        return cnt
```



## 链表

### 找出两个链表的交点

[力扣-160](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/)

![image-20201223001049495](https://gitee.com/turbobin_cao/images/raw/master/image-20201223001049495.png)

**解题思路：** 使 A 链接尾部连接到 B 链表的头部，B 链表的尾部连接到 A 链表的尾部，假设 A 和 B 公共的段为  c，A 独立的段为 a，B 独立的段为 b，可以得出 a+c+b = b+c+a，当两个指针走完后将会在交点相遇。

```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            # 当两个链表不相交时，最后 null = null 也成立
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA   
        return nodeA
```

### 链表反转

[力扣-206](https://leetcode-cn.com/problems/reverse-linked-list/description/)

![image-20201223002750126](https://gitee.com/turbobin_cao/images/raw/master/image-20201223002750126.png)

**解题思路：** 反转指针时，注意保持前驱节点，还需要一个临时变量保存下一个节点。

```python
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
```

### 归并两个有序的链表

[力扣-21](https://leetcode-cn.com/problems/merge-two-sorted-lists/description/)

![image-20201223003029868](https://gitee.com/turbobin_cao/images/raw/master/image-20201223003029868.png)

**解题思路：** 先创建一个哨兵头节点，使用归并排序的思想，两个链表逐步比较，归并到哨兵节点上

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l3 = ListNode(0)
        head = l3
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next	# 注意这行，要同时移动头指针
        head.next = l1 if l1 else l2	# 把未遍历的节点直接串联起来
        return l3.next
```

### 从有序链表中删除重复节点

[力扣-83](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/)

![image-20201223004509464](https://gitee.com/turbobin_cao/images/raw/master/image-20201223004509464.png)

**解题思路：** 使用一前一后两个指针，前后两个指针节点值相等时，直接删除后一个节点，否则前后指针都往后走一步。

```python
class Solution(object):
    def deleteDuplicates(self, head):
        prev = head
        curr = head
        while curr and curr.next:
            curr = curr.next
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = prev.next
        return head
```

### 删除链表的倒数第 n 个节点

[力扣-19](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/)

![image-20201223010802562](https://gitee.com/turbobin_cao/images/raw/master/image-20201223010802562.png)

**解题思路：** 使用一头一尾两个指针，尾指针先走，走到第 n 个节点，然后两个指针再同时向后移动。注意移动过程中保存前指针的前驱节点，方便做删除操作。

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        tail = head
        while n > 0:
            tail = tail.next
            n -= 1
        # 如果已经遍历到尾了，则直接删除头节点
        if not tail:
            return head.next
        curr = head
        while tail:
            prev = curr	# 保持前驱节点
            curr = curr.next
            tail = tail.next
        prev.next = prev.next.next
        return head
```

### 交换链表中的相邻结点

[力扣-24](https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/)

![image-20201223223548541](https://gitee.com/turbobin_cao/images/raw/master/image-20201223223548541.png)

**解题思路：** 使用前后两个指针指向第 1 和第 2 个节点，先断开第 2 个节点，再使第 2 个节点的 next 指针指向第 1 个节点，这时，第 1 个节点和第 2 个节点已经交换，还需要设置一个哨兵节点作为链表的头，哨兵节点的头指针指向第 2 个节点。第一步交换完成后，三个指针都继续向后移动。注意边界条件的判断，具体看如下代码：

```python
class Solution(object):
    def swapPairs(self, head):
        # 先判断边界条件
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        l = ListNode(0)     # 建一个哨兵节点
        pprev = l
        while curr:
            prev.next = curr.next
            curr.next = prev
            pprev.next = curr
            # 调整三个指针
            pprev = prev
            prev = prev.next
            if prev:
                curr = prev.next
            else:
                break	# 已经到末尾了，退出循环
        return l.next
```

### 链表求和

[力扣-445](https://leetcode-cn.com/problems/add-two-numbers-ii/description/)

![image-20201223233400606](https://gitee.com/turbobin_cao/images/raw/master/image-20201223233400606.png)

**解题思路：** 先遍历两个链表，使用两个栈来分别存储两个链表元素，然后分别从两个栈取出元素相加求和，然后逐步构造链表节点串联起来。由于相加涉及到数学逻辑，超过 10 需要进位，需要使用一个变量来保存进位的值。具体看如下代码：

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        l = ListNode(0)
        head = l
        c = 0   # c表示进位数
        while stack1 or stack2 or c > 0:
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            item = a + b + c
            c, val = divmod(item, 10)
            node = ListNode(val)
            # 每次在head和head.next之间插入新的节点
            node.next = head.next
            head.next = node
        return head.next
```

### 回文链表

[力扣-234](https://leetcode-cn.com/problems/palindrome-linked-list/description/)

![image-20201224002902712](https://gitee.com/turbobin_cao/images/raw/master/image-20201224002902712.png)

**解题思路：** 使用快慢两个指针，快指针每次走 2 步，慢指针每次走 1 步，当快指针走到末尾时，慢指针在中间节点，此时翻转后半段链表，最后使用一头一尾两个指针进行回文判断

```python
class Solution(object):
    def isPalindrome(self, head):
        # 利用快慢指针找到中间结点
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 反转slow到fast这后半段的链表
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # 比较前半段和后半段
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
```

### 固定分隔链表

[力扣-725](https://leetcode-cn.com/problems/split-linked-list-in-parts/description/)

![image-20201226220300208](https://gitee.com/turbobin_cao/images/raw/master/image-20201226220300208.png)

**解题思路：** 这题还是有点意思，整个链表分割成 k 个部分，每个部分要尽可能平均分，需要先知道链表的总长度，然后根据总长度求出分成 k 的部分的平均长度，由于不能刚好平均分，因此会存在余数。因为需要排在前面的长度比后面的长，因此需要把余数平摊分到前面的长度中。

```python
class Solution(object):
    def splitListToParts(self, root, k):
        # 先计算链表总长度
        n = 0
        head = root
        while head:
            n += 1
            head = head.next

        # 计算按k平均分的长度和余数
        avg_len, mod = divmod(n, k)
        result = []
        for i in range(k):
            # 如果有余数，就把余数往前平摊，得出这一段的限制长度
            limit = avg_len + 1 if mod > 0 else avg_len
            mod -= 1	# 余数减一
            node = ListNode(0)
            curr = node
            while limit > 0:
                curr.next = root
                curr = curr.next
                root = root.next
                limit -= 1
            curr.next = None    # 注意这里要断开与后一个节点的连接
            result.append(node.next)  
        return result
```

### 链表元素按奇偶重排

[力扣-328](https://leetcode-cn.com/problems/odd-even-linked-list/description/)

![image-20201226222757163](https://gitee.com/turbobin_cao/images/raw/master/image-20201226222757163.png)

**解题思路：** 此题不能使用额外的空间，也就是不能创建额外的链表节点，那么就只能使用临时变量来保存必要的节点了。链表奇偶重排，遍历的时候，需要奇节点每次往前走 2 步，偶节点每次往前走 2 步，最后奇链表和偶链表串联起来，具体看如下代码：

```python
class Solution(object):
    def oddEvenList(self, head):
        # 先判断边界情况
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = head.next   # 先保存偶数头结点
        while even and even.next:
            # 奇偶节点每次走2步
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        # 奇偶链表串联起来
        odd.next = even_head
        return head
```

## 栈和队列

### 用栈实现队列

[力扣-232](https://leetcode-cn.com/problems/implement-queue-using-stacks/description/)

**解题思路：** 队列是先进先出，栈是后进先出，如果要用栈来实现队列，需要使用两个栈，push 时数据存入第一个栈，pop 时如果判断第二栈是空，则把第一个栈的所有元素全部导入到第二个栈。

```python
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        # 第二个栈为空的时才需要把元素导过去
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        x = self.pop()
        self.stack2.append(x)
        return x

    def empty(self):
        if self.stack1 or self.stack2:
            return False
        return True
```

### 用队列实现栈

[力扣-225](https://leetcode-cn.com/problems/implement-stack-using-queues/description/)

**解题思路：** 对两个队列组合并不能实现栈，因为队列是先进先出，**组合之后并没有改变元素进出的顺序**，如果要用队列来实现栈，在 pop 操作时，需要把除最后进的元素以外的所有元素先出队，保存到另一个队列，然后再取出最后进的那个元素，操作完成后需要交换两个队列的作用，重复之前的操作。

```python
class MyStack(object):

    def __init__(self):
        self.queue = []
        self.queue2 = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        while len(self.queue) > 1:
            item = self.queue.pop(0)
            self.queue2.append(item)
        
        x = self.queue.pop(0)
        # 交换两个队列的作用
        self.queue, self.queue2 = self.queue2, self.queue
        return x

    def top(self):
        return self.queue[-1]

    def empty(self):
        return True if not self.queue else False
```

### 最小值栈

[力扣-155](https://leetcode-cn.com/problems/min-stack/description/)

![image-20201227142554758](https://gitee.com/turbobin_cao/images/raw/master/image-20201227142554758.png)

**解题思路：** 使用一个普通栈和一个最小值栈，普通栈就是正常的 push 和 pop 操作，最小值栈在 push 时需要与栈顶元素比较，每次都把最小的值 push 进去。需要注意的是，最小值栈需要和普通栈保持相同的元素个数，这样在 pop 时可以减少复杂的操作。如：顺序添加 1, 2, 3, 4, 5，普通栈元素：[1, 2, 3, 4, 5]，最小值栈元素：[1, 1, 1, 1, 1]。

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
            return
        m = self.min_stack[-1]
        m = min(x, m)
        self.min_stack.append(m)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

```

### 用栈实现括号匹配

[力扣-20](https://leetcode-cn.com/problems/valid-parentheses/description/)

![image-20201227143929601](https://gitee.com/turbobin_cao/images/raw/master/image-20201227143929601.png)

**解题思路：** 使用一个栈记录左括号，当遇到右括号时，从栈顶弹出一个括号进行匹配。最后要检查下栈是否空了，栈空了说明刚好全部匹配上了。

```python
class Solution(object):
    def isValid(self, s):
        stack = []
        match = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in match.values():
                stack.append(char)
            if not stack:
                return False
            if char in match and match[char] != stack.pop():
                return False
        # 检查栈是否为空
        return True if not stack else False
```

### 数组中元素与下一个比它大的元素之间的距离

[力扣 -739](https://leetcode-cn.com/problems/daily-temperatures/description/)

![image-20201227174440846](https://gitee.com/turbobin_cao/images/raw/master/image-20201227174440846.png)

**解题思路：** 

**方法一：** 暴力解法，针对每个元素都往后遍历找出第一个大于此元素的数组下标，两个下标相减即是两元素之间的距离。这种方法时间复杂度较高，在数组比较大时会导致超时。

```python
class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        result = [0] * n
        for i in range(n):
            j = i
            while j < n - 1:
                j += 1
                if T[i] < T[j]:
                    result[i] = j - i
                    break
        return result
```

**方法二：** 使用一个栈来保存那些未匹配的下一个比它大的元素，不过栈中保存的是数组下标，当遇到下一个比栈顶元素大的元素时，弹出栈顶元素，计算两下标的距离，再继续比较下一个栈顶元素。

```python
class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result
```

### 循环数组中比当前元素大的下一个元素

[力扣-503](https://leetcode-cn.com/problems/next-greater-element-ii/description/)

![image-20201227191523960](https://gitee.com/turbobin_cao/images/raw/master/image-20201227191523960.png)

**解题思路：** 这一题的解法与上一题类似，不同的是，这是一个循环数组，相当于需要遍历数组两次。注意本题输出的是元素，而不是元素下标。

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(n + n):
            num = nums[i % n]	# 用余数法计算下标值
            while stack and num > nums[stack[-1]]:
                j = stack.pop()
                result[j] = num
            if i < n:	# 小于n的下标才保存到栈中
                stack.append(i)
        return result
```

## 哈希表

### 两数之和

[力扣-1](https://leetcode-cn.com/problems/two-sum/description/)

![image-20201227203606388](https://gitee.com/turbobin_cao/images/raw/master/image-20201227203606388.png)

**解题思路：** 使用散列表保存数组元素与下标的对应关系，同时，散列表可以快速判断一个数是否存在。

```python
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            other = target - num
            if other in hashmap:
                return [hashmap[other], i]
            hashmap[num] = i
        return None
```

### 判断数组是否含有重复元素

[力扣-217](https://leetcode-cn.com/problems/contains-duplicate/description/)

![image-20201227204135834](https://gitee.com/turbobin_cao/images/raw/master/image-20201227204135834.png)

**解题思路：** 使用 hashset 结构进行判重，也可以使用 bitmap 结构。

```python
class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
```

### 最长和谐序列

[力扣-594](https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/)

![image-20201227205256269](https://gitee.com/turbobin_cao/images/raw/master/image-20201227205256269.png)

**解题思路：** 这题不太好理解，题目要求的是最长和谐子序列，但是不要求是元素连续的子序列。求最长和谐序列，那么，针对每个元素 num，必须要使 num+1 也在数组中，和谐序列的长度就是 num 与 num+1 元素个数的和。

```python
class Solution(object):
    def findLHS(self, nums):
        hashmap = {}
        # 统计每个元素的个数
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        longest = 0
        for num, cnt in hashmap.items():
            if (num + 1) not in hashmap:
                continue
            count = cnt + hashmap[num + 1]
            longest = max(longest, count)
        return longest
```

### 最长连续序列

[力扣-128](https://leetcode-cn.com/problems/longest-consecutive-sequence/description/)

![image-20201227223300020](https://gitee.com/turbobin_cao/images/raw/master/image-20201227223300020.png)

**解题思路：** 本题和上一题类似，不同的是需要找出连续的最长序列，只需要对每个元素不断加 1，并检查是否在数组中，记录加 1 的次数就是最长序列的长度。为了减少时间复杂度，可以判断当前元素减 1 是否在数组中，如果在，说明当前元素已经被统计过，跳过这次检查。为了快速判断元素是否在数组中，需要将数组转成 hashset

```python
class Solution(object):
    def longestConsecutive(self, nums):
        hashset = set(nums)
        longest = 0
        for num in hashset:
            # 优化逻辑，减小时间复杂度
            if (num - 1) in hashset:
                continue
            i = 1
            while (num + i) in hashset:
                i += 1
            longest = max(longest, i)
        return longest
```

## 字符串

### 两个字符串包含的字符是否完全相同

[力扣-242](https://leetcode-cn.com/problems/valid-anagram/description/)

![image-20201227225930194](https://gitee.com/turbobin_cao/images/raw/master/image-20201227225930194.png)

**解题思路：** 首先判断两个字符长度是否相同，然后将 s 构造成 hashmap，value 值为字符串出现的个数，遍历 t 中的字符，如果在字符串 s 的 hashmap 中存在，则个数减 1，最后成立的条件是 hashmap 中所有元素的个数都等于 0。

```python
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        for char in t:
            if char not in hashmap:
                return False
            if hashmap[char] <= 0:
                return False
            hashmap[char] -= 1
        return True
```

### 计算一组字符集合可以组成的回文字符串的最大长度

[力扣-409](https://leetcode-cn.com/problems/longest-palindrome/description/)

![image-20201227233106407](https://gitee.com/turbobin_cao/images/raw/master/image-20201227233106407.png)

**解题思路：** 先统计每个字符出现的次数，出现偶数次的字符都可以构造回文串，出现奇数次的，如果大于 2 次，最多可以取 cnt - 1 次，另外可以取 1 个出现奇数次的字符放中间。

```python
class Solution(object):
    def longestPalindrome(self, s):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        longest = 0
        odd = 0
        for char, cnt in hashmap.items():
            if cnt % 2 == 0:
                # 偶数的都满足条件
                longest += cnt
            elif cnt > 2:
                longest += (cnt - 1)
                odd = 1
            else:
                odd = 1
        return longest + odd
```

### 字符串同构

[力扣-205](https://leetcode-cn.com/problems/isomorphic-strings/description/)

![image-20201227235423254](https://gitee.com/turbobin_cao/images/raw/master/image-20201227235423254.png)

**解题思路：** 转化为比较下标数字是否相等，如 "egg"  -> [1, 2, 2]，"add" -> [1, 2, 2]，那么这两个字符串就是同构的。

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        s1 = []
        hashs = {}
        for i, char in enumerate(s):
            index = hashs.get(char, i)
            hashs[char] = index
            s1.append(index)

        t1 = []
        hasht = {}
        for i, char in enumerate(t):
            index = hasht.get(char, i)
            hasht[char] = hasht.get(char, i)
            t1.append(index)
        return s1 == t1
```

### 判断一个整数是否是回文数

[力扣](https://leetcode-cn.com/problems/palindrome-number/description/)

### 统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数

[力扣](https://leetcode-cn.com/problems/count-binary-substrings/description/)

## 树

### 树的高度

[力扣](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/)

### 平衡树

[力扣](https://leetcode-cn.com/problems/balanced-binary-tree/description/)

### 两节点的最长路径

[力扣](https://leetcode-cn.com/problems/diameter-of-binary-tree/description/)

### 翻转二叉树

[力扣](https://leetcode-cn.com/problems/invert-binary-tree/description/)

### 合并两棵树

[力扣](https://leetcode-cn.com/problems/merge-two-binary-trees/description/)

### 判断路径和是否等于一个数

[力扣](https://leetcode-cn.com/problems/path-sum/description/)

### 统计路径和等于一个数的路径数量

[力扣](https://leetcode-cn.com/problems/path-sum-iii/description/)

### 子树

[力扣](https://leetcode-cn.com/problems/subtree-of-another-tree/description/)

### 树的对称

[力扣](https://leetcode-cn.com/problems/symmetric-tree/description/)

### 二叉树最小深度

[力扣](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/)

### 统计左叶子节点的和

[力扣](https://leetcode-cn.com/problems/sum-of-left-leaves/description/)

### 相同节点值的最大路径长度

[力扣](https://leetcode-cn.com/problems/longest-univalue-path/)

### 间隔遍历

[力扣](https://leetcode-cn.com/problems/house-robber-iii/description/)

### 找出二叉树中第二小的节点

[力扣](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/)

### 一棵树每层节点的平均数

[力扣](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/)

### 得到左下角的叶子节点

[力扣](https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/)

### 非递归实现二叉树的前序遍历

[力扣](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/)

### 非递归实现二叉树的后序遍历

[力扣](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/)

### 非递归实现二叉树的中序遍历

[力扣](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/)

### 修剪二叉查找树

[力扣](https://leetcode-cn.com/problems/trim-a-binary-search-tree/description/)

### 寻找二叉查找树的第 k 个元素

[力扣](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/)

### 把二叉查找树每个节点的值都加上比它大的节点的值

[力扣](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/)

### 二叉查找树的最近公共祖先

[力扣](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

### 二叉树的最近公共祖先

[力扣](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

### 从有序数组中构造二叉查找树

[力扣](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/)

### 根据有序链表构造平衡的二叉查找树

[力扣](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/)

### 在二叉查找树中寻找两个节点，使它们的和为一个给定值

[力扣](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/)

### 在二叉查找树中查找两个节点之差的最小绝对值

[力扣](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/)

### 寻找二叉查找树中出现次数最多的值

[力扣](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/)

### 实现一个 Trie

[力扣](https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/)

### 实现一个 Trie，用来求前缀和

[力扣](https://leetcode-cn.com/problems/map-sum-pairs/description/)

## 双指针

### 有序数组的 Two Sum

[力扣](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/)

### 两数平方和

[力扣](https://leetcode-cn.com/problems/sum-of-square-numbers/description/)

### 反转字符串中的元音字符

[力扣](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/)

### 回文字符串

[力扣](https://leetcode-cn.com/problems/valid-palindrome-ii/description/)

### 归并两个有序数组

[力扣](https://leetcode-cn.com/problems/merge-sorted-array/description/)

### 判断链表是否存在环

[力扣](https://leetcode-cn.com/problems/linked-list-cycle/description/)

### 最长子序列

[力扣](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/description/)

## 排序

### 出现频率最多的 k 个元素

[力扣](https://leetcode-cn.com/problems/top-k-frequent-elements/description/)

### 按照字符出现次数对字符串排序

[力扣](https://leetcode-cn.com/problems/sort-characters-by-frequency/description/)

### 荷兰国旗问题(按颜色排序)

[力扣](https://leetcode-cn.com/problems/sort-colors/description/)

## 二分查找

### 求开方

[力扣](https://leetcode-cn.com/problems/sqrtx/description/)

### 找出大于给定元素的最小元素

[力扣](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/description/)

### 找出有序数组的单个元素

[力扣](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/description/)

### 第一个错误的版本

[力扣](https://leetcode-cn.com/problems/first-bad-version/description/)

### 旋转数组的最小数字

[力扣](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/)

### 有序数组中连续出现数字的区间

[力扣](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## 分治

### 给表达式加括号求值

[力扣](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/)

### 不同的二叉搜索树 II

[力扣](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/)

## 广度优先搜索(BFS)

### 计算在网格中从原点到特定点的最短路径长度

[力扣](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/)

### 组成整数的最小平方数数量

[力扣](https://leetcode-cn.com/problems/perfect-squares/description/)

### 最短单词路径

[力扣](https://leetcode-cn.com/problems/word-ladder/description/)

## 深度优先搜索(DFS)

### 岛屿的最大面积

[力扣](https://leetcode-cn.com/problems/max-area-of-island/description/)

### 岛屿的数量

[力扣](https://leetcode-cn.com/problems/number-of-islands/description/)

### 朋友圈数量

[力扣](https://leetcode-cn.com/problems/friend-circles/description/)

### 填充被围绕的区域

[力扣](https://leetcode-cn.com/problems/surrounded-regions/description/)

### 能到达的太平洋和大西洋的区域

[力扣](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/description/)

## 回溯算法

### 数字键盘组合

[力扣](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/)

### IP 地址划分

[力扣](https://leetcode-cn.com/problems/restore-ip-addresses/description/)

### 在矩阵中查找字符串

[力扣](https://leetcode-cn.com/problems/word-search/description/)

### 输出二叉树中所有从根到叶子的路径

[力扣](https://leetcode-cn.com/problems/binary-tree-paths/description/)

### 不含重复元素的全排列

[力扣](https://leetcode-cn.com/problems/permutations/description/)

### 含有相同元素的全排列

[力扣](https://leetcode-cn.com/problems/permutations-ii/description/)

### 组合问题

[力扣](https://leetcode-cn.com/problems/combinations/description/)

### 不含相同元素的组合求和

[力扣](https://leetcode-cn.com/problems/combination-sum/description/)

### 含有相同元素的组合求和

[力扣](https://leetcode-cn.com/problems/combination-sum-ii/description/)

### 1-9 数字的组合求和

[力扣](https://leetcode-cn.com/problems/combination-sum-iii/description/)

### 不含相同元素求子集

[力扣](https://leetcode-cn.com/problems/subsets/description/)

### 含有相同元素求子集

[力扣](https://leetcode-cn.com/problems/subsets-ii/description/)

### 分割字符串使得每个部分都是回文数

[力扣](https://leetcode-cn.com/problems/palindrome-partitioning/description/)

### N 皇后问题

[力扣](https://leetcode-cn.com/problems/n-queens/description/)

## 贪心算法

### 分配饼干

[力扣](https://leetcode-cn.com/problems/assign-cookies/description/)

### 不重叠的区间个数

[力扣](https://leetcode-cn.com/problems/non-overlapping-intervals/description/)

### 投飞镖刺破气球

[力扣](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

### 根据身高和序号重组队列

[力扣](https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/)

### 买卖股票最大的收益

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/)

### 买卖股票的最大收益 II

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

### 种植花朵

[力扣](https://leetcode-cn.com/problems/can-place-flowers/description/)

### 判断是否为子序列

[力扣](https://leetcode-cn.com/problems/is-subsequence/description/)

### 修改一个数成为非递减数组

[力扣](https://leetcode-cn.com/problems/non-decreasing-array/description/)

### 子数组最大的和

[力扣](https://leetcode-cn.com/problems/maximum-subarray/description/)

### 分隔字符串使同种字符出现在一起

[力扣](https://leetcode-cn.com/problems/partition-labels/description/)

## 动态规划

### 斐波那契数列

#### 爬楼梯问题

[力扣](https://leetcode-cn.com/problems/climbing-stairs/description/)

#### 强盗抢劫

[力扣](https://leetcode-cn.com/problems/house-robber/description/)

#### 强盗在环形街区抢劫

[力扣](https://leetcode-cn.com/problems/house-robber-ii/description/)

### 矩阵路径

#### 矩阵的最小路径和

[力扣](https://leetcode-cn.com/problems/minimum-path-sum/description/)

#### 矩阵的总路径数

[力扣](https://leetcode-cn.com/problems/unique-paths/description/)

### 数组区间

#### 数组区间和

[力扣](https://leetcode-cn.com/problems/range-sum-query-immutable/description/)

#### 数组中等差递增子区间的个数

[力扣](https://leetcode-cn.com/problems/arithmetic-slices/description/)

### 分割整数

#### 分割整数的最大乘积

[力扣](https://leetcode-cn.com/problems/integer-break/description/)

#### 按平方数来分割整数

[力扣](https://leetcode-cn.com/problems/perfect-squares/description/)

#### 分割整数构成字母字符串

[力扣](https://leetcode-cn.com/problems/decode-ways/description/)

### 最长子序列

#### 最长递增子序列

[力扣](https://leetcode-cn.com/problems/longest-increasing-subsequence/description/)

#### 一组整数对能够构成的最长链

[力扣](https://leetcode-cn.com/problems/maximum-length-of-pair-chain/description/)

#### 最长摆动子序列

[力扣](https://leetcode-cn.com/problems/wiggle-subsequence/description/)

#### 最长公共子序列

[力扣](https://leetcode-cn.com/problems/longest-common-subsequence/)

### 0-1 背包问题

#### 划分数组为和相等的两部分

[力扣](https://leetcode-cn.com/problems/partition-equal-subset-sum/description/)

#### 改变一组数的正负号使得它们的和为一给定数

[力扣](https://leetcode-cn.com/problems/target-sum/description/)

#### 01 字符构成最多的字符串

[力扣](https://leetcode-cn.com/problems/ones-and-zeroes/description/)

#### 找零钱的最少硬币数

[力扣](https://leetcode-cn.com/problems/coin-change/description/)

#### 找零钱的硬币数组合

[力扣](https://leetcode-cn.com/problems/coin-change-2/description/)

#### 字符串按单词列表分割

[力扣](https://leetcode-cn.com/problems/word-break/description/)

#### 组合总和

[力扣](https://leetcode-cn.com/problems/combination-sum-iv/description/)

### 股票交易

#### 需要冷却期的股票交易

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

#### 需要交易费用的股票交易

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/)

#### 只能进行两次的股票交易

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/)

#### 只能进行 k 次的股票交易

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/)

### 字符串编辑

#### 删除两个字符串的字符使它们相等

[力扣](https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/)

#### 编辑距离

[力扣](https://leetcode-cn.com/problems/edit-distance/description/)

#### 复制粘贴字符

[力扣](https://leetcode-cn.com/problems/2-keys-keyboard/description/)

