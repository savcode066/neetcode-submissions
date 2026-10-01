class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        for i in range(1, len(nums), 1):
            result.append(nums[i-1] * result[i-1])

        p = 1
        for i in range(len(nums)-2, -1, -1):
            p *= nums[i+1]
            result[i] *= p
        return result
