from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for word in strs:
            out[''.join(sorted(word))].append(word)
        return list(out.values())
        # hello giri