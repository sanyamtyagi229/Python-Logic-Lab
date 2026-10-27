class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longest(target):
            left = 0
            max_len = 0
            flips = 0
            for right in range(len(answerKey)):
                if answerKey[right] != target:
                    flips += 1
                while flips > k:
                    if answerKey[left] != target:
                        flips -= 1
                    left += 1
                max_len = max(max_len, right - left + 1)
            return max_len
        return max(longest('T'), longest('F'))