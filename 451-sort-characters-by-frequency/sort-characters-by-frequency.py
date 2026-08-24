class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        result=""
        pairs = c.most_common()
        res=[]
        for char,count in pairs:
            repeat=char*count
            res.append(repeat)
        result=result.join(res)
        return result