class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       # l = 0
        #r = k
        n = len(nums)
        window = set()
        for i in range(n):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
       
        return False  