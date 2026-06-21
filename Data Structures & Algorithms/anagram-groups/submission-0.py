class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Use THIS, not seen!
        
        for s in strs:
            sorte = "".join(sorted(s))
            res[sorte].append(s)  # Now it works!
        
        return list(res.values())