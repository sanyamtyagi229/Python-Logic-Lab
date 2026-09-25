class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        else:
            freq=Counter(nums)
            for x in freq.values():
                if x>2:
                    return False
        return True

        