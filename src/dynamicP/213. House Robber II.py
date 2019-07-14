'''
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
'''
def rob(nums):
    if not nums:return 0
    length=len(nums)
    if length<2:return nums[-1]
    dp1=[0]*length
    dp2=[0]*length
    dp1[1]=nums[0]
    dp2[1]=nums[1]
    for i in range(1,length-1):
        dp1[i+1]=max(dp1[i],dp1[i-1]+nums[i])
        dp2[i+1]=max(dp2[i],dp2[i-1]+nums[i+1])
    return max(dp1[-1],dp2[-1])

        
