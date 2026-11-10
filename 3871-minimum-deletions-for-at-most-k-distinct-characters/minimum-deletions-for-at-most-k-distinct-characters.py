class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freqs = Counter(s)
        if len(freqs) <= k:
            return 0
        sorted_counts = sorted(freqs.values())
        d = len(freqs) - k
        return sum(sorted_counts[:d])
        