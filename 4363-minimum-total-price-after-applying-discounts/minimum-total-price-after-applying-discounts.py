class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        i=0
        j=0
        while(i<len(prices)and j<len(discounts)):
            prices[i]=(prices[i]*(100-discounts[j]))/100
            i=i+1
            j=j+1
        return sum(prices)
