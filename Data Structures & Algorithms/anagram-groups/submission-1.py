class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        result = []
        for string in strs:
            count = [0] * 26

            for let in string:
                count[ord(let) - ord("a")] += 1

            if tuple(count) in strs_map:
                strs_map[tuple(count)].append(string)
            else:
                strs_map[tuple(count)] = [string]
        
        for value in strs_map.values():
            result.append(value)
        
        return result
        


        

        