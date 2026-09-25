class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        freq={}
        a=len(nums)//2
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for x in freq:
            if freq[x]==a:
                return x