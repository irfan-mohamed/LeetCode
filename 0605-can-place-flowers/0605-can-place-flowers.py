class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        counter = 0
        for i in range(l):
            if i == 0 and flowerbed[i] == 0:
                if flowerbed[(i+1)%l] != 1:
                    flowerbed[i] = 1
                    counter +=1
            if i == len(flowerbed)-1 and flowerbed[i] == 0:
                if flowerbed[(i-1)] != 1:
                    flowerbed[i] = 1
                    counter +=1
            if flowerbed[i] == 0 and flowerbed[(i+1)%l] != 1 and flowerbed[((i-1)+l)%l] != 1 :
                flowerbed[i] = 1
                counter +=1
        if counter >= n:
            return True
        else :
            return False