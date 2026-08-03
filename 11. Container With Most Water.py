class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left =0
        right=len(height)-1
        result = 0

        while left < right:
            d= right - left
            m= min(height[left], height[right])
            f= d*m

            if f > result:
                result = f
            elif height[left]> height[right]:
                right-=1
            else:
                left +=1
        return result
        
