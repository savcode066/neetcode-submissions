class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = "😃".join(strs)
        res += "😃"

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""
        for let in s:
            if let == "😃":
                res.append(temp)
                temp = ""
            else:
                temp += let
        return res



