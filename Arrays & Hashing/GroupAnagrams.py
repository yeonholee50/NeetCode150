class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        let's use collection and bucket of 26 index as the collection key and list of values as the list of str that fit 
        """
        hm = collections.defaultdict(list)
        for string in strs:
            bucket = [0] * 26
            for i in range(len(string)):
                c = string[i]
                bucket[ord(c) - ord('a')]+=1
            hm[tuple(bucket)].append(string)
        return hm.values()