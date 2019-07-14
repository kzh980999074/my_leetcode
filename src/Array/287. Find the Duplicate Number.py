'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Example 1:
Input: [1,3,4,2,2]
Output: 2
Example 2:
Input: [3,1,3,4,2]
Output: 3
索引的方法：数组A 中如果只出现一次  A[i] 表示索引 只出现一次/
'''
def findDuplicate(nums):

    for i in range(len(nums)):
        index=nums[i]

        if nums[index]>0:
            nums[index]=-nums[index]
        else:
            return index
    
