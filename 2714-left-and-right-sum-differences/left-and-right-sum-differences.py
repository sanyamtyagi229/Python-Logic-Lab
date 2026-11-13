class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        k = 0
        arr = []
        
        while k < len(nums):
            ls = 0
            rs = 0
            for i in range(0, k):
                ls += nums[i]
            for j in range(k + 1, len(nums)):
                rs += nums[j]
                
            arr.append(abs(ls - rs))
            k += 1
            
        return arr