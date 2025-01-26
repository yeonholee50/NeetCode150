class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for l in string:
                letters[ord(l) - ord('a')]+=1
            letters = tuple(letters)
            if hm[letters]:
                hm[letters].append(string)
            else:
                hm[letters] = [string]
        return list(hm.values())