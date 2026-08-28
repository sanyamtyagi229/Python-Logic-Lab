class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind=-1
        for i in range(len(word)):
            if word[i]==ch:
                ind=i
                break
        if ind==-1:
            return word
        arr = list(word)
        i, j = 0, ind
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
        return "".join(arr)
        