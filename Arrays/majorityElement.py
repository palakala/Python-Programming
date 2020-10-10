def majorityElement(nums):
        count = 0
        count1 = 0
        for i in range(len(nums)):
            if(count ==0):
                m = nums[i]
                count += 1
            else:
                if m == nums[i]:
                    count += 1
                else:
                    count -= 1
        for i in range(len(nums)):
            if nums[i] == m:
                count1 += 1
            else:
                continue
        l = len(nums)/2
        if count1>l:
            return m
        else:
            return False

nums = [2, 8, 7, 2, 2, 2, 2,1, 1]
print(majorityElement(nums))