def twoSum(self, nums, target):
    dictionary = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in dictionary:
            return [dictionary[complement], i]
        else:
            dictionary[num] = i
    return []
