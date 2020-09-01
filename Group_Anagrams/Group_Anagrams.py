class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrm_dict=dict()
        
        for i in range(len(strs)):
            word=''.join(sorted(strs[i]))
            #print(word)
            if word in angrm_dict:
                angrm_dict[word].append(i)
            else:
                angrm_dict[word]=[i]
        res=[]
        for vals in angrm_dict.values():
            tempres=[]
            for val in vals:
                tempres.append(strs[val])
            res.append(tempres)
        return(res)