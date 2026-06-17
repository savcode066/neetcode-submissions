class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s = {}
        letter_t = {}

        for let in s:
            if(let not in letter_s):
                letter_s[let] = 1
            else:
                letter_s[let]+=1
        
        for let in t:
            if(let not in letter_t):
                letter_t[let] = 1
            else:
                letter_t[let]+=1
        return letter_s == letter_t
