class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        ans = []
        for left, right in queries:
            range_xor = prefix[right + 1] ^ prefix[left]
            ans.append(range_xor)
            
        return ans