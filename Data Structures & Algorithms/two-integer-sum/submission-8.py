class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashset = set()
        # for i in range(len(nums)):  # [3,4,5,6] 7
        #     if target>nums[i]:
        #         hashset.add(target-nums[i])
        #     else:
        #         hashset.add(nums[i]-target)
        #     for j in range(len(nums)):
        #         if nums[j] in hashset and j != i:
        #             return [i,j]

        for i in range(len(nums)-1):   #[3,4,5,6] 
            for j in range(1,len(nums)):
                if (nums[i] + nums[j]) == target and i!=j:
                    return [i,j]

        