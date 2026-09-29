class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        lmax, rmax = height[left], height[right]
        count = 0
        while left +1 < right:
            if rmax >lmax:
                left +=1
                if height[left] > lmax:
                    lmax = height[left]
                else:
                    count += lmax - height[left]
            else:
                right-=1
                if height[right] > rmax:
                    rmax = height[right]
                else:
                    count += rmax - height[right]
        return count
            

        