from typing import List
class Solution:
    def reverse(self, nums : List[int], l: int, h: int) -> None:
        while l<h:
            nums[l], nums[h] = nums[h], nums[l]
            l += 1
            h -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, 0, n-1)
        return nums
s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))