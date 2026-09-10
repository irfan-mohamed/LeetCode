class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water_capacity = float('-inf')

        for i in range(0, len(height) - 1):
            if height[left] < height[right] or height[left] == height[right]:
                w = right - left
                h = height[left]

                max_water_capacity = max(w*h, max_water_capacity)

                left += 1

            elif height[right] < height[left]:
                w = right - left
                h = height[right]
                max_water_capacity = max(w*h, max_water_capacity)
                right -= 1

        return max_water_capacity

