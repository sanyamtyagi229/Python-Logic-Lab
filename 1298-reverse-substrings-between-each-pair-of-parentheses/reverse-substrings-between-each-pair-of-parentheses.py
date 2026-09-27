class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            # Find the first closing parenthesis
            right = s.find(')')
            # Find the closest opening parenthesis to its left
            left = s.rfind('(', 0, right)
            s = s[:left] + s[left + 1:right][::-1] + s[right + 1:]
            
        return s