'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.
Input: [2,1,5,6,2,3]
Output: 10
'''
def largestRectangleArea(heights):
    l=len(heights)
    if l==0:return 0
    if l==1:return heights[0]
    T=[[0]*i for i in range(1,l+1)]
    for i in range(l):
        T[i][0]=heights[i]
    count=1
    maxi=max(heights)
    while count<l:
        for i in range(count,l):
            T[i][count]=(min(T[i-1][count-1],T[i][count-1])/count)*(count+1)
            maxi=max(maxi,T[i][count])
        count+=1
        
    return int(maxi)
print(largestRectangleArea([2,1,5,6,2,3]))
        
         