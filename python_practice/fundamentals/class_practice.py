class MyClass:
    def __init__(self, nums):
        #Create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()

