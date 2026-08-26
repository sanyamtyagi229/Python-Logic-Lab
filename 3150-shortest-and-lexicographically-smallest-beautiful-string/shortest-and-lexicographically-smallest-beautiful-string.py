class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best_str = ""
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub.count('1') == k:
                    if best_str == "":
                        best_str = sub
                        
                    elif len(sub) < len(best_str):
                        best_str = sub
                        
                    elif len(sub) == len(best_str) and sub < best_str:
                        best_str = sub
                        
        return best_str