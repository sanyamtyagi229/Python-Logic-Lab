class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        dict={}
        for x in nums:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        for num,c in dict.items():
            if c>1:
                return num
        
        