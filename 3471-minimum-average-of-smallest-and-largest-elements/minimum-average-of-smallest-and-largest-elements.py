class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        i=0
        j=len(nums)-1
        c=[]

        while(i<j):
            a=nums[i]
            b=nums[j]
            avg=(a+b)/2
            c.append(avg)
            i+=1
            j-=1
        return min(c)

        