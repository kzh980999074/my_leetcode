'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
 You are asked to burst all the balloons. 
 If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. 
 After the burst, the left and right then becomes adjacent.
Find the maximum coins you can collect by bursting the balloons wisely.
Note:
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''
#确定哪一个是最后爆炸

def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l=len(nums)
        nums=[1]+nums+[1]
        dp=[[0 for i in range(l+2)] for i in range(l+2)]
        for i in range(1,l+1):
            dp[i][i]=nums[i]*nums[i-1]*nums[i+1]
        
        
        for i in range(1,l+1):
            for j in range(1,l+1-i):
                s=j
                e=j+i
                for k in range(s,e+1):
                    _max=dp[s][k-1]+dp[k+1][e]+nums[s-1]*nums[k]*nums[e+1]
                    dp[s][e]=max(_max,dp[s][e])
        print(dp)
        return dp[1][l]