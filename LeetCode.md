[[Code]]

# LeetCode
## 1. Two Sum
	Input: nums = [2,7,11,15], target = 9
	Output: [0,1]
	Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                       if nums[i] + nums[j] == target:
                            return[i,j]
```

Type: Array
Method: Brutal Force 
Difficulty: Easy
踩坑记录：def中：表示变量类型， ->提示返回类型

## 9. Palindrome Number
**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if(len(x) == 1): return True
        for i in range(int(len(x)/2)):
            if(x[i] != x[(len(x) - i - 1)]):
               return False
               break
            if(i == int(len(x)/2) - 1): return True
```

Type: String
Method: One Pass
Difficulty: Easy
踩坑记录：无

## 11. Container With Most Water
**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204221550204.png)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxarea = min(height[i], height[j]) * j
        while(i < j):
            if(height[i] <= height[j]):
                i += 1
                new = min(height[i], height[j]) * (j - i)
                maxarea = max(maxarea, new)
            else:
                j -= 1
                new = min(height[i], height[j]) * (j - i)
                maxarea = max(maxarea, new)
```

Type: Array
Method: Two Pointer Approach
Difficulty: Medium
踩坑记录：Brutal Force导致的Time Limit Exceeded → 木桶原理倒推，优化短板 → 首尾双指针 →O(n)时间复杂度

## 14. Longest Common Prefix
**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in range(1, len(strs), 1):
            ls = []
            if(len(strs[i]) == 0):
                pre = ""
                return pre
            num = min(len(pre), (len(strs[i])))
            for j in range(num):
                if(pre[j] == strs[i][j]):
                    ls.append(strs[i][j])
                else:
                    pre = "".join(ls)
                    break
                if(j == num - 1): pre = "".join(ls)
        return pre
```

Type: String
Method: Brutal Force
Difficulty: Easy
踩坑记录：考虑各种特殊情况

## 26. Remove Duplicates From Sorted Array
	Input: nums = [1,1,2]
	Output: 2, nums = [1,2,_]
	Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
	It does not matter what you leave beyond the returned k (hence they are underscores).

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ls = []
        for i in nums:
            if i not in ls:
                ls.append(i)
        for i in range(len(ls)):
            nums[i] = ls[i]
        return len(ls)
```

Type: Array
Method: Brutal Force
Difficulty: Easy
踩坑记录：`for i in range(len(nums))` -> `for i in nums`，列表赋值方法`nums = ls` -> `nums[i] = ls[i]`，`return len(num)`  -> `return len(ls)` 例子中`len(ls)`为2  `len(nums)`为3

## 27. Remove Element
	Input: nums = [3,2,2,3], val = 3
	Output: 2, nums = [2,2,_,_]
	Explanation: Your function should return k = 2, with the first two elements of nums being 2.
	It does not matter what you leave beyond the returned k (hence they are underscores).

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while 1:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)
```

Type: Array
Method: Brutal Force
Difficulty: Easy
踩坑记录：可以直接改成`while var in nums: nums.remove(val)`

## 35. Search Insert Position
	Input: nums = [1,3,5,6], target = 5
	Output: 2
	Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if(i == target):
                return nums.index(i)
                break
            if(i > target):
                return nums.index(i)
                break
            if(i == nums[-1]):
                return len(nums)
```

Type: Array
Method: Brutal Force
Difficulty: Easy
踩坑记录：超出最大值未考虑，可能还需要添加`if(nums[0] > target): return 0`

## 36. Valid Soduko
**Input:** board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
**Output:** true

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            lsrow = []
            for j in range(9):
                if(board[i][j].isnumeric()):
                    if(board[i][j] not in lsrow):
                        lsrow.append(board[i][j])
                    else: 
                        return False
        for i in range(9):
            lscolumn = []
            for j in range(9):
                if(board[j][i].isnumeric()):
                    if(board[j][i] not in lscolumn):
                        lscolumn.append(board[j][i])
                    else: 
                        return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
               lsnine = []
               lsnine.append(board[i][j])
               lsnine.append(board[i + 1][j])
               lsnine.append(board[i + 2][j])
               lsnine.append(board[i][j + 1])
               lsnine.append(board[i + 1][j + 1])
               lsnine.append(board[i + 2][j + 1])
               lsnine.append(board[i][j + 2])
               lsnine.append(board[i + 1][j + 2])
               lsnine.append(board[i + 2][j + 2])
               while('.' in lsnine):
                    lsnine.remove('.')
               if(len(set(lsnine)) != len(lsnine)): 
                    return False
        return True
```
Type: Array
Method: Brutal Force
Difficulty: Medium
踩坑记录：`append`只能添加单一元素，`isnumeric()`直接判断字符串类型，`set(object)`生成的子集无序

## 53. Maximum Subarray
**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** [4,-1,2,1] has the largest sum = 6.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        max = sum
        for i in range(1, len(nums)):
            if((sum + nums[i]) >= nums[i]): sum += nums[i]
            if((sum + nums[i]) < nums[i]): sum = nums[i]
            if(sum > max): max = sum
        return max
```

Type: Array
Method: Dynamic Programming, Kadane's Algorithm
Difficulty: Easy
踩坑记录：暴力循环超出time limit，**留出情况不处理**(> < 剩下的=)，大量无谓的`if`可以转`max`，以及不需要数位时直接`for i in nums`


## 58. Length of Last Word
**Input:** s = "Hello World"
**Output:** 5
**Explanation:** The last word is "World" with length 5.

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        ls = []
        for i in range(len(s)):
            if(s[i].isspace()): 
                if(count != 0):
                    ls.append(count)
                    count = 0
            else:
                count += 1
                if(i == len(s) - 1):
                    ls.append(count)
        return ls[-1]
```

Type: String
Method: Brutal Force
Difficulty: Easy
踩坑记录：字母结尾，多个空格，`str.isspace()`判断字符串为空

## 66. Plus One
	Input: digits = [1,2,3]
	Output: [1,2,4]
	Explanation: The array represents the integer 123.
	Incrementing by one gives 123 + 1 = 124.
	Thus, the result should be [1,2,4].
	
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
                break
            else:
                digits[i] = 0
                if(i == 0):
                    digits.insert(0, "1")
                    return digits
                    break
```

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        num = "".join(digits)
        num = eval(num) + 1
        digits = []
        for i in str(num):
            digits.append(i)
        return digits
```

Type: Array
Method: Brutal Force
Difficulty: Easy
踩坑记录：`insert`用法，`join`依赖的变量类型，不同形式变量之间的转换


## 88. Merge Sorted Array
	Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
	Output: [1,2,2,3,5,6]
	Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
	The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if((m == 0) & (n == 0)): 
            nums1[:] = []
        elif(m == 0): 
            nums1[:] = nums2[:n]
        elif(n == 0): 
            nums1[:] = nums1[:m]
        else:
            nums1[:] = nums1[:m] + nums2[:n]
            nums1.sort()
```

Type: Array
Method: Brutal Force
Difficulty: Easy
踩坑记录：`array`赋值`[:]`，字符串不同切片方式

## 118. Pascal's Triangle
**Input:** numRows = 5
**Output:** [1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]，外头还有一层数组

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = []
        for i in range(numRows):
            new = []
            for j in range(i + 1):
                if((j == 0) | (j == i)):
                    new.append(1)
                else:
                    num = ls[(i - 1)][(j - 1)] + ls[(i - 1)][j]
                    new.append(num)
            ls.append(new)
        return ls
```

Type: Array
Method: Brutal Force
Difficulty: Easy
踩坑记录：[1]和[1,1]直接用+连接的话是[1,1,1]而非嵌套列表，需要通过`list.append(object)`来实现，运算符优先级问题加括号

## 119. Pascal's Triangle II
**Input:** rowIndex = 3
**Output:** [1,3,3,1]

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ls = []
        prev = []
        for i in range(rowIndex + 1):
            new = []
            for j in range(i + 1):
                if((j == 0) | (j == i)):
                    new.append(1)
                else:
                    num = prev[j - 1] + prev[j]
                    new.append(num)
            prev[:] = new
        return new
```
Type: Array
Method: Brutal Force
Difficulty: Easy
踩坑记录：运算符优先级

## 121. Best Time to Buy and Sell Stock
**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minvalue = float('inf')
        for i in range(len(prices)):
            minvalue = min(minvalue, prices[i])
            maxp = max(maxp, prices[i] - minvalue)
        return maxp
```
Type: Array
Method: One Pass
Difficulty: Easy
踩坑记录：一端极大，一端极小，所以从一端开始循环，实时加入极小，实时改变极大。

## 125. Valid Palindrome
**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = str.lower(s)
        if(s[::-1] == s): return True
        else: return False
```

Type: String
Method: Built-in Function
Difficulty: Easy
踩坑记录：`str.isalnum()`判断是否为字母数字

## 168. Excel Sheet Column Title
**Input:** columnNumber = 701
**Output:** "ZY"

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        new = columnNumber
        length = 0
        weight = 1
        while(new > 0):
            new -= pow(26, weight)
            weight += 1
            length += 1
        out = ""
        for i in range(length):
            if(columnNumber > 26):
                num = int((columnNumber - 1) / pow(26, length - i - 1))
            else:
                num = int(columnNumber / pow(26, length - i - 1))
            a = chr(num + 64)
            out += a
            columnNumber -= num * pow(26, length - i - 1)
        return out
```

Type: String
Method: Brutal Force
Difficulty: Easy
踩坑记录：`length`没法直接判断得出，即$column$是$26$的几次方，最后一位特殊处理（不保0），ASCII码直接转换数字和字母

## 171. Excel Sheet Column Number
**Input:** columnTitle = "ZY"
**Output:** 701

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        weight = pow(26, length - 1)
        sum = 0
        for i in columnTitle:
            sum += weight * (ord(i) - 64)
            weight /= 26
        return int(sum)
```

Type: String
Method: Brutal Force
Difficulty: Easy
踩坑记录：`ord`和`chr`可以用于ASCII码和字符互转，返回时加`int`

## 242. Valid Anagram
**Input:** s = "anagram", t = "nagaram"
**Output:** true

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls1 = []
        ls2 = []
        for i in s:
            ls1.append(i)
        for j in t:
            ls2.append(j)
        ls1.sort()
        ls2.sort()
        if(ls1 == ls2): return True
        else: return False
```

Type: String
Method: Built-In Function
Difficulty: Easy
踩坑记录：`list.sort()`没有返回值

## 243. Shortest Word Distance
**Input:** wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
**Output:** 3

```python
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ls1 = []
        ls2 = []
        for i in range(len(wordsDict)):
            if(wordsDict[i] == word1):
                ls1.append(i)
        for j in range(len(wordsDict)):
            if(wordsDict[j] == word2):
                ls2.append(j)
        ls = []
        mindis = float('inf')
        for i in ls1:
            for j in ls2:
                diff = abs(i - j)
                mindis = min(mindis, diff)
        return int(mindis)
```

Type: String
Method: Brutal Force
Difficulty: Easy
踩坑记录：无

## 293. Flip Game
**Input:** currentState = "++++"
**Output:** ["--++","+--+","++--"]

```python
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ls = []
        new = []
        if(len(currentState) <= 1): return []
        for i in range(len(currentState) - 1):
            new = list(currentState)
            if((currentState[i] == "+") & (currentState[i + 1] == "+")):
               new[i] = "-"
               new[i + 1] = "-"
               new = ''.join(new)
               ls.append(new)
        return ls
```

Type: String
Method: Brutal Force
Difficulty: Easy
踩坑记录：字符串没法改特定位数，需要转换成列表再转回字符串

## 344. Reverse String
**Input:** s = ["h","e","l","l","o"]
**Output:** ["o","l","l","e","h"]

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
```

Type: String
Method: Built-In Function
Difficulty: Easy
踩坑记录：转字符串再转列表，忽略内置函数