class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin and cmax track the minimum and maximum possible number of open '('
        cmin = 0
        cmax = 0
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                cmax += 1 # if '*' is treated as '('
                cmin -= 1 # if '*' is treated as ')'
            
            # If max open count is negative, we have too many ')'
            if cmax < 0:
                return False
            
            # min open count can't be negative, so we reset it to 0
            # (this just means we chose to treat some '*' as empty instead of ')')
            if cmin < 0:
                cmin = 0
                
        # If the minimum possible open parentheses is 0, the string is valid
        return cmin == 0