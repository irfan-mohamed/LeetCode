class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for i in range(len(nums)):
            if nums[i] in set_:
                return True
            else :
                set_.add(nums[i])
        return False