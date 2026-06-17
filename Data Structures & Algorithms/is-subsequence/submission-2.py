class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        s_index = 0
        for i in range(len(t)):
            
            if s[s_index] == t[i]:
                s_index += 1

            if s_index == len(s):
                return True
        return False



        