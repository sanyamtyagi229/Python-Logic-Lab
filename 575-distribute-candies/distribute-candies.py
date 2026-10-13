class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        dic={}
        for i in candyType:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        return min(len(dic), len(candyType) // 2)
        

        