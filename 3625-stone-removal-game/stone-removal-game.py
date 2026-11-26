class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        size=10
        needed=0
        compl=0
        while size>=1:
            if needed+size<=n:
                needed=needed+size
                compl+=1
                size-=1
            else:
                break
        if compl%2==1:
            return True
        else:
            return False

