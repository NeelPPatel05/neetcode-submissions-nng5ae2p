class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
           encoded += s + "$#$"
           #string abcde --> abcde$ 
        return encoded

    def decode(self, s: str) -> List[str]:
        print (s)
        strs = []
        j = 0
        i = 0
        word = ""
        while (i < len(s)):
            print (i)
            if (s[i:i+3] != "$#$"):
                word += s[i]
                i+=1
            else:
                strs.append(word)
                j += 1
                word = ""
                i+=3
        return strs



        
