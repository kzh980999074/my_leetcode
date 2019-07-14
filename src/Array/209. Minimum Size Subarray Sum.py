'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, 
return 0 instead.Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

def minSubArrayLen(self, s, nums):
    sums=0
    start=0
    end=0
    l=len(nums)
    min_len=-1
    for i in range(nums):
        if nums[i]>s:return 1
        sums+=nums[i]
        if sums>=s:
            end=i
            sums-=nums[i]
            min_len=i
            break
    if min_len<0:return 0
    while end<l:
        sums+=nums[end]
        s1=start
        for i in range(s1,end):
            sums-=nums[i]
            start+=1
            if sums>=s:
                min_len=min(end-start,min_len)
            else:
                break
        end+=1
    return min_len+1