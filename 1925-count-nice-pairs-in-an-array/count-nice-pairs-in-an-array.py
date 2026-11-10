class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        v = []
        for num in nums:
            orig = num
            rev = 0
            while num != 0:
                d = num % 10
                rev = rev * 10 + d
                num = num // 10
            v.append(orig - rev)
        
        v.sort()
        
        ans = 0
        current_count = 1  
        for i in range(1, len(v)):
            if v[i] == v[i-1]:
                current_count += 1
            else:
                ans += (current_count * (current_count - 1)) // 2
                current_count = 1  
        ans += (current_count * (current_count - 1)) // 2
        
        return ans % (10**9 + 7)