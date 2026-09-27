class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        ss=0
        sd=0
        for i in range(len(nums)):
            if nums[i]<10:
                ss+=nums[i]
            else:
                sd+=nums[i]
        if ss>sd:
            return True
        elif ss<sd:
            return True
        else:
            return False
        