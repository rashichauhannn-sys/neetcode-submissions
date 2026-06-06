class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored_nums = sorted(nums)
        return any(a == b for a, b in 
        pairwise(stored_nums))