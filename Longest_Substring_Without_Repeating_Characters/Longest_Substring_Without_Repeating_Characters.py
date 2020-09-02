class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        len_sub=0
        seen=dict()
        #print(type(seen))
        while r < len(s):
            if s[r] in seen.keys():
                l=max(seen[s[r]]+1,l)
            len_sub=max(r-l+1,len_sub)
            seen[s[r]]=r
            r+=1
                    
        return len_sub