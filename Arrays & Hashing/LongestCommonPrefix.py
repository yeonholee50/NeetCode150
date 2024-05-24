class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        lp = ""
        common = True
        counter = 0
        same = False
        maximum = max([len(string) for string in strs])
        while common == True:
            for i in range(len(strs)):
                if i == 0:
                    if counter >= len(strs[i]):
                        common = False
                        same = True
                        break
                    lp = lp + strs[i][counter]
                elif counter >= len(strs[i]) or lp[-1] != strs[i][counter]:
                        common = False
                        break
            if counter == maximum:
                same = True  
            counter+=1
        if same == False:
            return lp[:-1]
        else:
            return lp