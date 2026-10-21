class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        
        while l < r:
            w = r - l
            min_h = min(height[l], height[r])
            cura = w * min_h
            area = max(area, cura)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1   
        return area