import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 #가장 작은수부터 시작
        min_price = sys.maxsize #가장 큰 수 부터 시작

        for price in prices:
            min_price = min(min_price, price) #최소값 갱신
            profit = max(profit, price-min_price) #이익 갱신

        return profit