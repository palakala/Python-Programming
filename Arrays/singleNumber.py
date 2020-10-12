def singleNumber(nums):
        ans = 0
        for i in range(len(nums)):
            ans = ans^nums[i]
        return ans
nums = [1,2,1]
print(singleNumber(nums))