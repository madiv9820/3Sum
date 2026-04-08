from typing import List

class pySolution:
    def py_threeSum(self, nums: List[int]) -> List[List[int]]:
        # 🎯 Final result list (no set needed since we handle duplicates inline)
        triplets_With_Zero_Sum: List[List[int]] = []

        # 🔄 Sort the array (required for two-pointer approach + duplicate handling)
        nums.sort()
        n: int = len(nums)

        # 🔁 Fix the first element of the triplet
        for i in range(n):

            # 🚫 Skip duplicate values for the first element
            # Ensures we don't generate duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 👈👉 Initialize two pointers
            start_Index: int = i + 1      # left pointer
            end_Index: int = n - 1        # right pointer

            # 🔁 Find pairs such that sum = -nums[i]
            while start_Index < end_Index:

                # ➕ Current sum of triplet
                current_Sum: int = nums[i] + nums[start_Index] + nums[end_Index]

                # 🎯 Case 1: Found valid triplet
                if current_Sum == 0:

                    # 📥 Add triplet to result
                    triplets_With_Zero_Sum.append([
                        nums[i], 
                        nums[start_Index], 
                        nums[end_Index]
                    ])

                    # ➡️ Move left pointer forward
                    start_Index += 1

                    # 🚫 Skip duplicates for second element
                    # Prevents repeating same triplet
                    while (
                        start_Index < end_Index and 
                        nums[start_Index] == nums[start_Index - 1]
                    ):
                        start_Index += 1

                # ⬆️ Case 2: Sum too large → decrease it
                elif current_Sum > 0:
                    end_Index -= 1

                # ⬇️ Case 3: Sum too small → increase it
                else:
                    start_Index += 1

        # 🔄 Return all unique triplets
        return triplets_With_Zero_Sum