class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        k=0
        for i in range(len(nums)):
            c=0
            while(nums[i]!=0):
                d=nums[i]%10
                c=c+1
                nums[i]//=10
            if c%2==0:
                k=k+1
            
        return k
            
        