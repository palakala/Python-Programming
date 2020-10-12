class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0]*101
        for val in nums:
            count[val] += 1
        # prefix sum
        for i in range(1,101):
            count[i] += count[i-1]
        #traverse
        result = [0]*len(nums)
        
        for i, val in enumerate(nums):
            if val>0:
                result[i] = count[val-1]
        return result