# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# for time complexity, would it be possible to sort the array, split arrays in half and see if can hit the target?

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]


print(twoSum([3,2,4], 6))