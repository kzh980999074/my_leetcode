'''
Given an array of non-negative integers, you are initially positioned 
at the first index of the array.Each element in the array represents your maximum jump length 
at that position.Your goal is to reach the last index in the minimum number of jumps.
Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

def jump(nums):
    length=len(nums)
    if length<=1:return 0
    count=1
    start=0
    end=1
    maxi=nums[0]
    while maxi<length-1:
        start=maxi
        for i in range(end,maxi+1):
            maxi=max(maxi,nums[i]+i)
        end=start+1
        coount+=1
    return count
