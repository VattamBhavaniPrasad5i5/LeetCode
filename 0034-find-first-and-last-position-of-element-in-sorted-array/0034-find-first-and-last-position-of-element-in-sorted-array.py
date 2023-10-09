class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            if nums[low] < target:
                low += 1
            elif nums[high] > target:
                high -= 1
            elif nums[low] == target and nums[high] == target:
                return [low, high]
        return [-1, -1]