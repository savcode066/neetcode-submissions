class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = (right+left)//2
            print("right: ", right)
            print("left: ", left)
            print("mid: ", mid)

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                print("target: ", target)
                print("nums[left]: ", nums[left])
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return -1

        