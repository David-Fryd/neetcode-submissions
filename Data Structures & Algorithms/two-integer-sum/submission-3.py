class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = {}

        for idx,val in enumerate(nums):
            if val in solutions:
                return [solutions[val], idx]
            else: 
                complement = target - val
                solutions[complement] = idx



    # nums = [3,4,5,6], target = 7
    # Output: [0,1]

    # ( if i see 4, answer is 0 and curr number)

    # ( if i see)