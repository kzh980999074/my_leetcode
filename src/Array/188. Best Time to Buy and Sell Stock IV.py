'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''
def maxProfit(prices):
    l=len(prices)
    if l<=1:return 0
    if l==2:return max(0,prices[1]-prices[0])
    profits=[]
    for i in range(l-1,0,-1):
        prices[i]=prices[i]-prices[i-1]
    index=2
    profit=prices[1]
    print(prices)
    while index<l:
        if profit>=0 and prices[index]>=0:
            profit+=prices[index]
            index+=1
        elif profit<=0 and prices[index]<=0:
            profit+=prices[index]
            index+=1
        else:
            profits.append(profit)
            profit=prices[index]
            index+=1
    profits.append(profit)
    print(profits)
prices=[3,2,6,5,0,3,1,3,9,6,4,6,8,5,4,2,6,8,6,4,3,1,12,2]
maxProfit(prices)



def maxProfit1( k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    
    dp = [0] * len(prices)
    for _ in range(k):
        buy = dp[0] - prices[0]
        for j in range(1,len(prices)):
            tmp = max(dp[j-1], prices[j] + buy)
            buy = max(buy, dp[j] - prices[j])
            dp[j] = tmp
        print(dp)
    return dp[-1]
maxProfit1(4,prices)
