class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l=0
        h=len(numbers)-1
        while(l<h):
            mid=numbers[l]+numbers[h]
            if mid==target:
                return [l+1,h+1]
            elif(mid>target):
                h=h-1
            else:
                l=l+1

        return[]

        