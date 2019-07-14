'''
iven an array nums of n integers and an integer target, are there elements a, b, c, and d 
in nums such that a + b + c + d = target? Find all unique quadruplets 
in the array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[[-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]]
'''

#需要去掉重复的
        
def threeSum(nums, target,val0):
    l=len(nums)
    result=[]
    if l<=2 : return target
    i=1
    while  i<l-1:
        left=0
        right=l-1
        while left<i and right>i:
            value=nums[i]+nums[left]+nums[right]
            if value>target:
                right-=1
            elif value<target:
                left+=1
            else:
                result.append([val0,nums[left],nums[i],nums[right]])
                right-=1
                left+=1
                while nums[right]==nums[right+1] and right>i:
                    right-=1
                while nums[left]==nums[left-1] and left<i:
                    left+=1
        i+=1
    return result


def fourSum(nums, target):

    result=[]
    l=len(nums)
    if l<4:return result
    nums.sort()
    for i in range(0,l-3):
        arri=threeSum(nums[i+1:],target-nums[i],nums[i])
        result.extend(arri)
    return result


arr=[-3,-2,-1,0,0,1,2,3]
result=fourSum(arr,0)
print(result)