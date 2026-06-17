class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(heights[right], heights[left]) * abs(right - left)

        n = len(heights)

        right = n - 1
        left = 0
        curr_area = min(heights[right], heights[left]) * abs(right - (left))
        while(left<right):
            print(left, " ", right)
            current = min(heights[right], heights[left]) * abs(right - (left))
            curr_area = max(curr_area, current)
            if ( heights[right] > heights[left]):
                left += 1
            else:
                right -= 1
        return curr_area
