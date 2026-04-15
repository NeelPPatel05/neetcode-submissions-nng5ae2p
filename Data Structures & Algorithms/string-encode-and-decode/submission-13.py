class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
           encoded += str(len(s)) + "#" + s
           #string abcde --> 5#abcde
           #indexes          01234567
        return encoded

    def decode(self, s: str) -> List[str]:
        print (s)
        strs = []
        j = 0
        i = 0
        hash_pos = 0
        while (i < len(s)):
            for j in range (i, len(s)):
                if (s[j] == "#"):
                    hash_pos = j
                    break 
            print ("index:" + str(i))
            print("hash: " + str(hash_pos))
            print(s[i: hash_pos])
            size = int(s[i: hash_pos])
            strs.append(s[hash_pos+1: hash_pos+1+size])
            print("increasing index by ..." + str(hash_pos+1))
            i = hash_pos+size+1
        return strs



        
