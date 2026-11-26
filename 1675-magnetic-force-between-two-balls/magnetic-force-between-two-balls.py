class Solution:
    def helper(self,position:list[int] ,m: int,minforce:int)->bool:
        ballplaced=1
        last=position[0]
        for i in range(1,len(position)):
            cb=position[i]
            gap=cb-last
            if gap>=minforce:
                ballplaced+=1
                last=cb
                if ballplaced==m:
                    return True
        return False
            

    def maxDistance(self, position: list[int], m: int) -> int:
        
        position.sort()
        left = 1
        right = position[-1] - position[0]
        best_force = 1

        while left <= right:
            mid = left + (right - left) // 2

            if self.helper(position, m, mid):
                best_force = mid
                left = mid + 1
            else:
                right = mid - 1

        return best_force
