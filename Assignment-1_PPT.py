''' 
**Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
def twoSum(nums, target):
    num_dict = {} 
    
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num  
        
        if complement in num_dict:
            return [num_dict[complement], i]  
        num_dict[num] = i  
    return []  

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]


''' 
**Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.
'''
def removeElement(nums, val):
    i = 0  
    
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]  
            i += 1  
    
    return i  
nums = [3, 2, 2, 3]
val = 3

k = removeElement(nums, val)
print(k)  # Output: 2
print(nums)  # Output: [2, 2, _, _]

'''

Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5
Output: 2

'''
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
nums = [1, 3, 5, 6]
target = 5

index = searchInsert(nums, target)
print(index)  # Output: 2

'''
**Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

'''
def plusOne(digits):
    n = len(digits)
    
    
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    
    digits.insert(0, 1)
    return digits
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]


'''

**Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

'''
def merge(nums1, m, nums2, n):
    i = m - 1  # pointer for nums1
    j = n - 1  # pointer for nums2
    k = m + n - 1  # pointer for the merged array
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # Copy the remaining elements from nums2 if any
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


'''
Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

'''
def containsDuplicate(nums):
    unique_values = set()
    
    for num in nums:
        if num in unique_values:
            return True
        unique_values.add(num)
    
    return False
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)  # Output: True

'''
**Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

'''

def moveZeroes(nums):
    n = len(nums)
    i = 0  # pointer for the next position to place a nonzero element
    
    for j in range(n):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    
    # Fill the remaining positions with zeros
    while i < n:
        nums[i] = 0
        i += 1
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

'''

Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]
'''
def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    
    for num in nums:
        if num in num_set:
            duplicate = num
        else:
            num_set.add(num)
    
    for i in range(1, n+1):
        if i not in num_set:
            missing = i
            break
    
    return [duplicate, missing]
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)  # Output: [2, 3]
