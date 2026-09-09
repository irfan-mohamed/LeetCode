class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
            
            
            