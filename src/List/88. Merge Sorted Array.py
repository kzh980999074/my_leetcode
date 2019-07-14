'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) 
    to hold additional elements from nums2.
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
'''
def merge(nums1,m,nums2,n):
    if n !=0:
        l=n+m-1
        l1=m-1
        l2=n-1
        while l>=0:
            if nums1[l1]>nums2[l2]:
                nums1[l]=nums1[l1]
                l-=1
                l1-=1
            else:
                nums1[l]=nums2[l2]
                l-=1
                l2-=1
            print(l,l1,l2)
            if l1<0 or l2<0:
                break
        for i in range(l2+1):
            nums1[i]=nums2[i]
    
    print(nums1)
n1=[2,0]
n2=[1]
merge(n1,1,n2,1)