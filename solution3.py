class solution3:
    def maxprofit(self,prices:list[int])->int:
        left,profit=0,0
        for right in range(1,len(prices)):
            if prices[left]<prices[right]:
                profit(max(profit,prices[right]-prices[left]))
            else:
                left = right
        return profit
