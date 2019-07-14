'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

def find(nums1,nums2,l1,l2,i,j,k):
    if k<=1:
        return (i,j)
    if j>l2:
        return (i+k,-1)
    if i>l1:
        return (j+k,-2)
    val=(k-1)//2
    val1=val
    val2=k-val1
    if i+val1>=l1:
        val1=l1-1-i
        val2=k-val1
    elif j+val2>=l2:
        val2=l2-j-1
        val1=k-val2    

    if nums1[val1+i]>nums2[val2+j]:
        k-=val2
        j+=val2+1
        return find(nums1,nums2,l1,l2,i,j,k)
    elif nums1[val1+i]<nums2[val2+j]:
        k-=val1
        i+=val1+1
        return find(nums1,nums2,l1,l2,i,j,k)
    else:
        return (i,j)

print(find([1,3,4,5,8,9],[2,4,4,10],6,4,0,0,5))    
            
    
    