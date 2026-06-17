class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        reference = strs[0]
        ans = ""
        for i in range(len(reference)):
            for s in strs:
                if i >= len(s) or s[i] != reference[i]:
                        return ans
            ans += reference[i]
        
        return ans

         

        
        