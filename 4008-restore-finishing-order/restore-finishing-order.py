class Solution:
    def recoverOrder(self, nums: List[int], friends: List[int]) -> List[int]:
        seen=set(friends)
        c=[]
        for x in nums:
            if x in seen:
                c.append(x)
        return c
        
        