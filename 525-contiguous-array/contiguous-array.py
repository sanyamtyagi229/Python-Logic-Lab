class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ps = 0
        ml = 0
        dic = {0: -1}
        
        for i, x in enumerate(nums):
            if x == 0:
                ps -= 1
            else:
                ps += 1
                
            if ps in dic:
                l = i - dic[ps]
                ml = max(ml, l)
            else:
                dic[ps] = i
                
        return ml