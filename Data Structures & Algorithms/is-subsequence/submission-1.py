class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        if len(s) == 1:
            if s in t:
                return True
            else:
                return False

        s_index = 0
        for i in range(len(t)):

            if s_index == len(s) - 1:
                return True
            
            if s[s_index] == t[i]:
                s_index += 1
        return False



        