class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append('(')
            else:
                # Sum up all scores inside the current parentheses pair
                current_score = 0
                while stack and stack[-1] != '(':
                    current_score += stack.pop()
                
                # Pop the matching '('
                stack.pop()
                
                # If it was an empty '()', score is 1. Otherwise, 2 * score.
                score = 1 if current_score == 0 else 2 * current_score
                stack.append(score)
                
        # The stack now contains top-level scores; sum them up to get the final answer
        return sum(stack)