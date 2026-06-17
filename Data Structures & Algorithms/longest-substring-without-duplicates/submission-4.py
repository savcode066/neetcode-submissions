class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in sub_string:
                sub_string.remove(s[l])
                l += 1
            sub_string.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length
            
             