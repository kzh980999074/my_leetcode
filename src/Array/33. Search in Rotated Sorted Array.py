'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

def search(nums, target):
    if not nums:
        return -1
    l=len(nums)
    if l==1:
        return 0 if nums[0]==target else -1
    s=0
    e=l-1
    p=-1
    if nums[s]==target:return s
    if nums[e]==target:return e
    while s+1<e:
        if nums[s]==nums[e]:
            s+=1
            e-=1
            if nums[s]==target:return s
            if nums[e]==target:return e
        elif nums[s]<nums[e]:
            if target<nums[s] or target>nums[e]:
                return -1
            q=(s+e)//2
            print(s,e,q,'*')
            if nums[q]==target:
                return q
            elif nums[q]>target:
                e=q
            else:
                s=q
        else:
            q=(s+e)//2
            if nums[q]==target:
                return q
            elif nums[q]<nums[e]:
                if target>nums[q] and target<nums[e]:
                    s=q
                else:
                    e=q
            else:
                if target>nums[s] and target<nums[q]:
                    e=q
                else:
                    s=q
    return -1
arr=[4,5,6,7,0,1,2]
print(search(arr,1))