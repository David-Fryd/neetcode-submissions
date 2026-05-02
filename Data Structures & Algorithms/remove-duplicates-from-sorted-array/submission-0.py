class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_seen = nums[0]
        idx = 1
        num_removed = 0
        while idx < len(nums):
            if nums[idx] == last_seen:
                nums.pop(idx)
                num_removed += 1
            else:
                last_seen = nums[idx]
                idx+=1
        return len(nums)