class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = ""
        for x in range(0, len(strs[0])):
            ch = strs[0][x]
            for s in strs[1:]:
                if x >= len(s) or s[x] != ch:
                    return prefix    
            prefix += ch
        return prefix
