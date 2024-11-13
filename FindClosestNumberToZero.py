class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest    
        
