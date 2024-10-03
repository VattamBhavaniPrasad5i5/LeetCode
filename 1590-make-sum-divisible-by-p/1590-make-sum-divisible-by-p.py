class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total_sum = sum(nums) ## sum of nums
        remainder = total_sum % p ## remainder that total_sum divided by p

        if remainder == 0:
            return 0 ## if remainder is 0, it means it is already divisible by p

        prefix_mod_map = {0:-1} ## make prefix_mod_map
        current_sum = 0 ## current_sum
        min_length = len(nums) ## set min_length

        for i, num in enumerate(nums):
            current_sum += num 
            mod = current_sum % p
            target_mod = (mod - remainder) % p

            if target_mod in prefix_mod_map: ## if we find target mod in prefix_mod_map
                min_length = min(min_length, i - prefix_mod_map[target_mod]) ## min_length will be i - prefix_mod_map[target_mod]

            prefix_mod_map[mod] = i ## store prefix_mod_map[mod] at index i

        return min_length if min_length < len(nums) else -1 ## return min_length (if it's impossible to return the length of the smallest subarray, return -1)