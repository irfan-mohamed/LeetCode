class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            key = num
            if key in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        result = [[] for _ in range(len(nums) + 1)]
        for num, count in hashmap.items():
            result[count].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for num in result[i]:
                res.append(num)
                if len(res) == k:
                    return res
