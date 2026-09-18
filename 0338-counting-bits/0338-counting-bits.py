class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i >> 1 is identical to i // 2
            # i & 1 tracks if the number is odd (ends in 1) or even (ends in 0)
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans