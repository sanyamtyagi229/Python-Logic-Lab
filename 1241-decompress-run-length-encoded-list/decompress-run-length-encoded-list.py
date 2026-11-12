class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        l=[]
        i=0
        j=1
        while j<len(nums):
            count=nums[i]
            while count!=0:
                l.append(nums[j])
                count-=1
            i=i+2
            j=j+2
        return l
        