class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        counter = 0
        for i in range(l):
            if flowerbed[i] == 0 :
                left_empty = i == 0 or flowerbed[i-1] != 1
                right_empty = i == l-1 or flowerbed[i+1] != 1
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    counter += 1
        if counter >= n:
            return True
        else :
            return False