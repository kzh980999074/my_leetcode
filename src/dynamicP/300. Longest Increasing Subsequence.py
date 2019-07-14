'''
Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note: 
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
'''

def lengthOfLIS(nums):
    if not nums:
        return 0
    inc=[nums[0]]
    l=len(nums)
    j=1
    for i in range(1,l):
        if nums[i]>inc[-1]:
            inc.append(nums[i])
            j+=1
        else:
            if j==1:
                inc[0]=min(inc[0],nums[i])
            else:
                for k in range(j-1,0,-1):
                    if inc[k]>nums[i] and inc[k-1]<nums[i]:
                        inc[k]=nums[i]
    return j



    