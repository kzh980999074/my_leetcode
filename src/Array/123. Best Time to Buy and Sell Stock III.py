'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
'''
def maxprofit(prices):
    l=len(prices)
    if l<=1:return 0
    if l==2:return max(0,prices[1]-prices[0])
    right=[0]*l;left=[0]*l
    val1=prices[0];val2=prices[-1]
    for i in range(1,l):
        left[i]=max(left[i-1],prices[i]-val1)
        val1=min(val1,prices[i])
        right[l-i-1]=max(right[l-i-1],val2-prices[l-i])
        val2=max(val2,prices[l-i])
    profit=0
    for i in range(l):
        profit=max(left[i]+right[i],profit)
    print(profit)
    return profit

prices=[3,3,5,0,0,3,1,4]
maxprofit(prices)
