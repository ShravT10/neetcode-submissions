class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # res = [] #nums = [1,2,3,4]
        # prefix = []
        # postfix = []

        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix.insert(i,nums[i])
                
        #     else:
        #         prefix.insert(i,nums[i]*prefix[i-1])
                
        # for i in range(1,len(nums)+1):
        #     if i == 1:
        #         postfix.insert(-i,nums[-1])
        #     else:
        #         postfix.insert(-i,nums[-i]*postfix[-i+1])

        # for i in range(0,len(nums)):
        #     if i == 0:
        #         res.append(postfix[i+1])
        #     elif i+1 == len(nums):
        #         res.append(prefix[-2])
        #     else:
        #         res.append(prefix[i-1]*postfix[i+1])

        # return res

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        