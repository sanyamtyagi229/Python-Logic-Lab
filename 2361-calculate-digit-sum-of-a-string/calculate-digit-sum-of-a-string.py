class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            news = []
            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                digitsum = sum(int(char) for char in chunk)
                news.append(str(digitsum))
            s = "".join(news)
        return s