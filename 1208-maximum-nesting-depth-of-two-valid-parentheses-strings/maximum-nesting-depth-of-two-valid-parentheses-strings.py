class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign to 0 or 1 based on current depth parity
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrease depth first, then match the parity of the opening bracket
                depth -= 1
                ans.append(depth % 2)
                
        return ans