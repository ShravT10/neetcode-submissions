class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        arr = sorted([v for k,v in hashmap.items()])

        return [K for K,v in hashmap.items() if v in arr[-k::]]