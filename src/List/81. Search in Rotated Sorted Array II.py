


def seach(nums,target):
    l=len(nums)
    if l==1:
        return target==nums[0]
    result=False
    e=l-1
    s=0
    if target==nums[s] or target==nums[e]:return True
    while (not result)  and e>s+1:
        if nums[e]==nums[s]:
            e-=1
            s+=1
            if nums[e]==target or nums[s]==target:
                result=True
        else:
            mid=(e+s)//2
            if nums[mid]==target:
                result=True

            if nums[e]>nums[s]:
                if nums[mid]>target:
                    e=mid
                else:
                    s=mid
            else:
                if nums[mid]>target:
                    if nums[e]>=nums[mid] :
                        e=mid
                    elif nums[s]>=nums[mid] and nums[s]<target:
                        e=mid
                    else:
                        s=mid
                else:#target >
                    if nums[mid]>=nums[s]:
                        s=mid
                    elif nums[e]>=nums[mid] and nums[e]>target:
                        s=mid
                    else:
                        e=mid
    print(result)
arr=[4,5,6,7,0,1,2]
seach(arr,5)
            
            
                                        
        