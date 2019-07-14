'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
def searchRange(nums, target):

    position=[-1,-1]
    if not nums:return position
    l=len(nums)
    s=0;e=l-1
    if nums[s]==target and nums[e]==target:
        return [s,e]
    if nums[s]>target or nums[e]<target:return position
    if l==2:
        if nums[s]==target:
            return [0,0]
        if nums[e]==target:
            return [1,1]
        else:
            return [-1,-1]
    p=-1
    if nums[s]==target:
        p=s
    elif nums[e]==target:
        p=e
    else:
        while s+1<e:
            q=(e+s)//2
            if nums[q]==target:
                p=q
                break
            elif nums[q]>target:
                e=q
            else:
                s=q
    if p==-1:
        return position
    else:
        s=p
        e=p
        for i in range(s-1,-1,-1):
            if nums[i]!=nums[i+1]:
                s=i+1
                break
        for j in range(e+1,l):
            if nums[j]!=nums[j-1]:
                e=j-1
                break
        return [s,e]
print(searchRange([1,2,3,4,5,5,6],6))