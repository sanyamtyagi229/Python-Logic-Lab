class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for x in nums:
            while x!=0:
                d=x%10
                if d==digit:
                    count+=1
                x=x//10
        return count