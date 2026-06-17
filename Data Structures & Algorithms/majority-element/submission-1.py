class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_hash = {}

        for n in nums:
            if n in counter_hash:
                counter_hash[n] += 1
            else:
                counter_hash[n] = 1
        for num in counter_hash:
            if counter_hash[num] > (len(nums)//2):
                return num
        

