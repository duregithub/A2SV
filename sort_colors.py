class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        one = 0
        t = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
                
            elif nums[i] == 1:
                one += 1
            else:
                t += 1
        counter = 0
        for i in range(len(nums)):
            if z != 0:
                nums[counter] = 0
                counter += 1
                z -= 1
            elif one != 0:
                nums[counter] = 1
                counter += 1
                one -= 1
            else:
                nums[counter] = 2
                counter += 1
                t -= 1



