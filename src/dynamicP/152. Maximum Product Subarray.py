'''
Given an integer array nums, 
find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''

def maxProduct(nums):
    length=len(nums)
    if length<2:return nums[0]
    
    else:
        dynamic=[[0,0] for i in range(length)]
        dynamic[0][0]=max(nums[0],0)
        dynamic[0][1]=min(nums[0],0)
        maxi=dynamic[0][0]
        for i in range(1,length):
            dynamic[i][0]=max(dynamic[i-1][0]*nums[i],nums[i]*dynamic[i-1][1],0,nums[i])
            dynamic[i][1]=min(dynamic[i-1][0]*nums[i],nums[i]*dynamic[i-1][1],0,nums[i])
            maxi=max(dynamic[i][0],maxi)
        return maxi

