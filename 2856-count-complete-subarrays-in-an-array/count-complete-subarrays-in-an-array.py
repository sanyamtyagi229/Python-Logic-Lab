class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        target_distinct = len(dic)

        complete_count = 0
        for i in range(n):
            sub_freq = {}
            distinct_count = 0

            for j in range(i, n):
                val = nums[j]
                if val not in sub_freq or sub_freq[val] == 0:
                    sub_freq[val] = 1
                    distinct_count += 1
                else:
                    sub_freq[val] += 1
                if distinct_count == target_distinct:
                    complete_count += 1

        return complete_count