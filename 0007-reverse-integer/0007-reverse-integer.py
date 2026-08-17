class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        res = 0
        # Work with the absolute value to handle digits cleanly
        # Track the sign separately
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Pre-check overflow before updating res
            # For positive result boundary check
            if sign == 1:
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > INT_MAX % 10):
                    return 0
            # For negative result boundary check
            else:
                # abs(INT_MIN) is 2147483648. INT_MIN // 10 holds the absolute division bound.
                if res > abs(INT_MIN) // 10 or (res == abs(INT_MIN) // 10 and pop > abs(INT_MIN) % 10):
                    return 0
            
            res = res * 10 + pop
            
        return res * sign
