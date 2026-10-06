class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            hashmap.setdefault(''.join(sorted(i)), []).append(i)         
        
        return [v for k,v in hashmap.items()]