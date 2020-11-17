class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums), 0
        snums = nums[:]
        snums.sort()
        for i in range(len(nums)):
            if(nums[i] != snums[i]):
                start = min(start, i)
                end = max(end, i)
        if end-start > 0:
            return end - start + 1
        else:
            return 0
            
 """
 Problem Statement:

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1 :

Input: [2, 6, 4, 8, 10, 9, 15] 

Output: 5 

Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order. 
 """
