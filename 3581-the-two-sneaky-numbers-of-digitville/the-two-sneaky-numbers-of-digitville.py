class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        dict={}
        for x in nums:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        for num, count in dict.items():
            if count==2:
                a.append(num)
        return a
        