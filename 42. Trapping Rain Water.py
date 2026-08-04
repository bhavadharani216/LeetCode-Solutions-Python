class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        water =0
        maxleft=height[left]
        maxright = height[right]


        while(left < right):
            if(maxleft < maxright):
                left+=1
                maxleft=max(maxleft , height[left])
                water = water + (maxleft- height[left])
            
            else:
                right-=1
                maxright = max(maxright, height[right])
                water  = water + (maxright - height[right])
    
        return water
        
