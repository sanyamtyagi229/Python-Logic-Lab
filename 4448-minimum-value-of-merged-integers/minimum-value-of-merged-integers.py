class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = []
        for i in range(0,len(nums)-1,2):
            x = nums[i]
            y = nums[i+1]
            new_num = str(x) + str(y)
            ans.append(int(new_num))


        return min(ans)
            
            
        