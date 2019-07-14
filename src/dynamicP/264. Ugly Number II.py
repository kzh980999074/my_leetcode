'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
'''
from collections import deque
def uglyNumber(n):
    nums=deque([0,1,2,3,4,5])
    i2=2
    i3=3
    i5=5
    if n<=5:
        return nums[n]
    count=5
    num=6
    status=True
    while count<n:
        if num%2==0:
            val=num//2
            for i in range(i2,count):
                if nums[i]>val:
                    if nums[i-1]==val:
                        nums.append(num)
                        count+=1
                        i2=i-1
                        status=False
                    else:
                        break
        if status:
            if num%3==0:
                val=num//3
                for i in range(i3,count):
                    if nums[i]>val:
                        if nums[i-1]==val:
                            nums.append(num)
                            count+=1
                            i3=i-1
                            status=False
                        else:
                            break
        if status:
            if num%5==0:
                val=num//5
                for i in range(i5,count):
                    if nums[i]>val:
                        if nums[i-1]==val:
                            nums.append(num)
                            count+=1
                            i5=i-1
                            status=False
                        else:
                            break     
        num+=1
        status=True
    print(nums[n])
    print(nums)
                    
                    
def uglyNumber1(n):

    nums=[0]*n
    nums[0]=1
    p2=0;p3=0;p5=0
    count=1
    while count<n:
        f2=nums[p2]*2
        f3=nums[p3]*3
        f5=nums[p5]*5
        mini=min(f2,f3,f5)
        nums[count]=mini
        if mini==f2:
            p2+=1
        if mini==f3:
            p3+=1
        if mini==f5:
            p5+=1
        count+=1w
    print(nums[-1])
    print(nums)
    
uglyNumber1(1)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    