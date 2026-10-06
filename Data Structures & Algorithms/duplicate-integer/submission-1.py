class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # d_set = set()

        # for i in nums:
        #     if i in d_set:
        #         return True
        #     else:
        #         d_set.add(i)
        # return False
        
        return len(list(set(nums))) != len(nums)