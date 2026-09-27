class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack1 = []
        
        for i in s:
            if i == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
                
        for i in t:
            if i == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
                
        return stack == stack1