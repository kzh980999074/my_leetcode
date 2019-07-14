'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''
#def search(self, nums: List[int], target: int) -> bool:



def search(nums,target):
    l=len(nums)
    if l <3:
        if target in nums:return True
        else:return False
    i=0;j=len(nums)-1
    
    while j>=i:
        if nums[i]==target or nums[j] ==target:
            return True
        else:
            if nums[i]==nums[j]:
                i+=1
                j-=1
            elif nums[j]>nums[i]:
                if binary_find(nums,i,j,target):
                    return True
            else:
                m=(i+j)//2
                if target==nums[m]:
                    return True
                else:
                    if nums[m]>nums[i] or nums[m]>nums[j]:
                        if binary_find(nums.i,m,target):
                            return True
                        else:
                            i=m+1
                            j-=1
                    else:
                        if binary_find(nums,m,j,target):
                            return True
                        else:
                            j=m-1
                            i+=1
    return False
    







def binary_find(nums,i,j,target):  
    if nums[i]>target or nums[j]<target:return False
    if j-i<2:return False
    while j-i>1:
        m=(j+i)//2
        if target==nums[m]:
            return True
        elif target>nums[m]:
            i=m
        else:
            j=m
    return False













'''

#find povit point
def find_pivot(nums,l_1,l_2):
    if l_2-l_1<2:
        if nums[l_2]>nums[l_1]:
            return nums[l_1]
        else:
            return nums[l_2]
    l_m=(l_1+l_2)//2
    if nums[l_m]>nums[l_1]:
        return find_pivot(nums,l_m,l_2)
    elif nums[l_m]==nums[l_1]:
        status=acsending(nums,l_1,l_m)
        if status[0]:
            return status[1]
        else:
            return find_pivot(nums,l_m,l_2)
    else:
        return find_pivot(nums,l_1,l_m)       
def acsending(nums,i,j):
    for k in range(i,j):
        if nums[i]>nums[i+1]:
            return (1,nums[i+1])
        else:
            return (0,nums[i])
'''



