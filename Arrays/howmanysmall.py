def smallNumbers(nums):
    newArray = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                count += 1
        newArray.append(count)
    return newArray
nums = [6,5,4,8]
print(smallNumbers(nums))