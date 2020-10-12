from collections import defaultdict
def singleNumber(nums):
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1
    
    for i in hash_table:
        if hash_table[i] == 1:
            return i
nums = [1,2,1]
print(singleNumber(nums))