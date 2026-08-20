class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]

            old_max = current_max 
            old_min = current_min

            current_max = max([num, old_max * num, old_min * num])
            current_min = min([num, old_max* num, old_min * num])

            result = max(current_max, result)
        return result