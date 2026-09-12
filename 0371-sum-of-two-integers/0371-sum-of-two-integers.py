class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFF
        while b != 0:
            sum_without_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

            a = sum_without_carry
            b = carry

        if a <= 0x7FFFFFF:
            return a
        else:
            return ~(a ^ mask)