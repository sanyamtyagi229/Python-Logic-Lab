class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid is on the increasing slope, the peak is to the right
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            # If mid is on the decreasing slope, the peak is to the left (or is mid)
            else:
                r = mid
                
        return l