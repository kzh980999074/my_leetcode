'''
Given a collection of distinct integers, return all possible permutations.
'''
def permute(nums):
        result=[]
        def helper(nums,element=[]):
            if len(nums)==1:
                element.append(nums[0])
                result.append(element)
            for i in range(len(nums)):
                element1=element.copy()
                element1.append(nums[i])
                nums1=nums[:i]
                nums1.extend(nums[i+1:])
                helper(nums1,element1)
        helper(nums)
        return result