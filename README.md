# LeetCode 题解

[toc]

## 数组与矩阵

### 把数组中的 0 移到末尾

[力扣-283](https://leetcode-cn.com/problems/move-zeroes/description/)

![image-20201213110155042](https://gitee.com/turbobin_cao/images/raw/master/image-20201213110155042.png)

**解题思路**：

**方法一：**首先想到的是可以利用冒泡的思想，将等于 0 的元素依次挪到最后。这里有个优化，每次都判断下是否有元素交换，如果没有交换则可以直接退出循环。冒泡的时间复杂度为 O(n<sup>2</sup>)。

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

**方法二：**利用指针，先把不等于 0 的元素往前挪，剩余的数字全部赋值 0。时间复杂度接近 O(n)。

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

**解题思路：**如果要重塑一个矩阵，那么前后元素总数必须是相同的，并且(行数 * 列数) 的积必须相等，此外遍历元素的时候还要注意列元素满了要换行，具体看如下代码。

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

**解题思路：**这题一不小心就想复杂了，其实就是简单的计数，然后比较最大值

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

**方法一：**搜索算法，一般想到广度优先搜索(BFS)或深度优先搜索(DFS)。该选哪一种呢？如果是 BFS，起点的选择很重要，如果直接从左上角搜索到右下角，最坏情况复杂度较高，将导致超时，合适的起点位置应该是右上角或左下角，并在搜索过程中不断调整搜索方向；如果选择 DFS，则建议选择中间位置开始搜索，如果比目标值小，则往右下角搜索，否则往左上角搜索。

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

**方法二：**因为这是一个有序矩阵，可以使用类似二分查找的算法。起点同样选择从右上角开始搜索。

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

**方法一：**求 top k 或者求第 k 大、第 k 小元素，一般采用堆来求解。第 k 大元素使用小顶堆，第 k 小元素则使用大顶堆。编程语言中一般实现的是优先级队列，这是一个小顶堆结构，而求解第 k 小元素可以转化为求第 `n-k+1` 大元素。

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

**方法二：**由于这是一个升序排序的数组，可以使用二分查找，每次先查找一半，看是否达到了第 k 大元素。

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

**方法一：**利用 bitmap 的思想，申请一个长度为 n+1 的数组，存放 1~n 的整数，从下标 1 开始遍历，值为 0 的则为缺失的元素，值为 2 的则为重复的元素。

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

**方法二：**通过交换元素的方式使得数组下标与元素对齐，最后遍历找出未对齐的元素和下标即为所求。

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

**解题思路：**按本题的要求：不能使用额外空间，也不能更改原数组，也就是不能使用 bitmap 解法，也不能通过交换元素的方式来求解。那么只有使用双指针了，但是这是一个无序数组，也不能按常规的双指针解法。解题方法还是比较难想到，由于这是一个 1~n 范围的数组，只有一个重复的元素，可以根据元素值**跳转到对应的下标**来访问元素，由于存在重复的元素，访问的路径最后会构成一个环，如 [1,3,4,2,2] 的访问，访问的元素为 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 ......，题目变成了求解环的入口，可以使用快慢指针来求解。

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

**解题思路：**首先要求出数组的度，即求出每个元素出现的次数的最大值，还要求出拥有相同度的最短连续子数组，其实就是求相同元素第一次出现的下标和最后一次出现的下标，两个下标之差就是连续子数组的长度。

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

**解题思路：**遍历元素，判断 `matrix[i][j]` 与 `matrix[i+1][j+1]` 是否相等。注意边界条件的判断。

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

**解题思路：**不断根据元素的值跳到对应下标，为防止出现访问路径变成环，需要对访问过的位置进行标记，同时记录访问路径的长度，最后求出长度的最大值。

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

**解题思路：**转化为求有多少个元素可以与下标对齐，相邻元素可以交换。

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

[力扣](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/)

### 链表反转

[力扣](https://leetcode-cn.com/problems/reverse-linked-list/description/)

### 归并两个有序的链表

[力扣](https://leetcode-cn.com/problems/merge-two-sorted-lists/description/)

### 从有序链表中删除重复节点

[力扣](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/)

### 删除链表的倒数第 n 个节点

[力扣](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/)

### 交换链表中的相邻结点

[力扣](https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/)

### 链表求和

[力扣](https://leetcode-cn.com/problems/add-two-numbers-ii/description/)

### 回文链表

[力扣](https://leetcode-cn.com/problems/palindrome-linked-list/description/)

### 固定分隔链表

[力扣](https://leetcode-cn.com/problems/split-linked-list-in-parts/description/)

### 链表元素按奇偶重排

[力扣](https://leetcode-cn.com/problems/odd-even-linked-list/description/)

## 栈和队列

### 用栈实现队列

[力扣](https://leetcode-cn.com/problems/implement-queue-using-stacks/description/)

### 用队列实现栈

[力扣](https://leetcode-cn.com/problems/implement-stack-using-queues/description/)

### 最小值栈

[力扣](https://leetcode-cn.com/problems/min-stack/description/)

### 用栈实现括号匹配

[力扣](https://leetcode-cn.com/problems/valid-parentheses/description/)

### 数组中元素与下一个比它大的元素之间的距离

[力扣](https://leetcode-cn.com/problems/daily-temperatures/description/)

### 循环数组中比当前元素大的下一个元素

[力扣](https://leetcode-cn.com/problems/next-greater-element-ii/description/)

## 哈希表

### 两数之和

[力扣](https://leetcode-cn.com/problems/two-sum/description/)

### 判断数组是否含有重复元素

[力扣](https://leetcode-cn.com/problems/contains-duplicate/description/)

### 最长和谐序列

[力扣](https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/)

### 最长连续序列

[力扣](https://leetcode-cn.com/problems/longest-consecutive-sequence/description/)

## 字符串

### 两个字符串包含的字符是否完全相同

[力扣](https://leetcode-cn.com/problems/valid-anagram/description/)

### 计算一组字符集合可以组成的回文字符串的最大长度

[力扣](https://leetcode-cn.com/problems/longest-palindrome/description/)

### 字符串同构

[力扣](https://leetcode-cn.com/problems/isomorphic-strings/description/)

### 回文子字符串个数

[力扣](https://leetcode-cn.com/problems/palindromic-substrings/description/)

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

