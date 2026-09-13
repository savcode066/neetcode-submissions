class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited = set()

        max_length = 0
        for num in nums_set:
            if num in visited:
                continue
            length = 1
            
            visited.add(num)
            current = num + 1

            while current in nums_set:
                if current in visited:
                    break
                visited.add(current)
                current += 1
                length += 1

            current = num - 1
            
            while current in nums_set:
                if current in visited:
                    break
                visited.add(current)
                current -= 1
                length += 1
            max_length = max(max_length, length)
        return max_length


        

        