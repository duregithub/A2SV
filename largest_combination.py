class Solution:
    def combo(self, nums):

        output = ""
        container = []
        tenth = []
        for i in range(len(nums)):
            if nums[i] % 10 == 0:
                tenth.append(str(nums[i]))
                continue
            container.append(str(nums[i]))

        container.sort(reverse = True)
        tenth.sort(reverse = True)
        print(container)
        print(tenth)

        for i in range(len(container)):
            output += container[i]
        for i in range(len(tenth)):
            output += tenth[i]
        return output
    
s = Solution()
print(s.combo([111311, 1113]))


