'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 3
Output: [1,3,3,1]
Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:return [1]
        if rowIndex==1:return [1,1]
        row=rowIndex//2+2
        result=[1]*row
        for i in range(2,rowIndex+1):
            for j in range(i//2,0,-1):
                result[j]=result[j]+result[j-1]
            if i%2==1:
                result[i//2+1]=result[i//2]
        if rowIndex%2==0:
            result=result[:-1]
            return result+list(reversed(result[:-1]))
        else:
            result
            return result+list(reversed(result[:-2]))