class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        swap strat
        0000110010011022200210020
        """
        n = len(nums)
        flag = True

        while flag:
            flag = False
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    flag = True
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        