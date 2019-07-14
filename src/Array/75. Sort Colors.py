'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
 with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

def sortColor(nums):
    l=len(nums)
    if l<=1:return
    i=0;j=l-1;k=0
    while k<l:
        if nums[k]==0:
            nums[k],nums[i]=nums[i],nums[k]
            k+=1
            i+=1
        elif nums[k]==2:
            nums[k],nums[j]=nums[j],nums[k]
            j-=1
            l-=1
        else:
            k+=1
nums=[2,0,2,1,1,0]
sortColor(nums)
print(nums)