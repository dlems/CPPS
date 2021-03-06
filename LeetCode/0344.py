"""
https://leetcode.com/problems/reverse-string/

344. Reverse String
Easy

# =======================================
# Description
# =======================================

Write a function that reverses a string. The input string is given as an array 
of characters char[].

Do not allocate extra space for another array, you must do this by modifying the 
input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


# ---------------------------------------
# Example 1:
# ---------------------------------------
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


# ---------------------------------------
# Example 2:
# ---------------------------------------
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


# ==============================================================================
# My solution
# ==============================================================================

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


# ============================================================================== 
# LeetCode solution 1 - Recursion, In-Place, O(N) Space
# ==============================================================================
"""
Does in-place mean constant space complexity?

No. By definition, an in-place algorithm is an algorithm which transforms input 
using no auxiliary data structure. 

The tricky part is that space is used by many actors, not only by data structures.
The classical example is to use recursive function without any auxiliary data 
structures.
    - Is it in-place? Yes.
    - Is it constant space? No, because of recursion stack.


# ---------------------------------------
# Complexity Analysis
# ---------------------------------------
- Time complexity
    - O(N) time to perform N/2 swaps.

- Space complexity
    - O(N) to keep the recursion stack.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


# ============================================================================== 
# LeetCode solution 2 - Two Pointers, Iteration, O(1) Space
# ==============================================================================
"""
Two Pointers Approach
    - In this approach, two pointers are used to process two array elements at 
      the same time. 
    - Usual implementation is to set one pointer in the beginning and one at the 
      end and then to move them until they both meet.


# ---------------------------------------
# Complexity Analysis
# ---------------------------------------
- Time complexity
    - O(N) time to perform N/2 swaps.

- Space complexity
    - O(1), it's a constant space solution.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1