class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list1 = []
        # list3 = []
        # for i in range(len(strs)):
        #     if strs[i] in list3 :
        #         continue
        #     list2 = [strs[i]]
        #     for j in range(i+1, len(strs)):
        #         if (sorted(list(strs[i])) == sorted(list(strs[j]))):
        #             list2.append(strs[j])
        #             list3.append(strs[j])
        #     list1.append(list2)
        # return list1
        hashmap = dict()
        for string in strs:
            key = "".join(sorted(string))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(string)
        list1 = []
        for value in hashmap:
            list1.append(hashmap[value])
        return list1
            
            
            