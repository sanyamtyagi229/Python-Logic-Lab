class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        a=[]
        dict={}
        for x in nums:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        for num, count in dict.items():
            if count>1:
                a.append(num)
        return a
        