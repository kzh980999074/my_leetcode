

def permuteUnique(nums):
    ans=[[]]
    for n in nums:
        new_ans=[]
        for l in ans:
            for i in range(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n:break
        print(new_ans)
        ans=new_ans
    return ans
print(permuteUnique([1,1,2]))