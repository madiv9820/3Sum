from typing import List, Set, Tuple

class pySolution:
    def py_threeSum(self, nums: List[int]) -> List[List[int]]:
        # 🎯 Set to store UNIQUE triplets (as tuples)
        # Automatically removes duplicates 🚫
        triplets_With_Zero_Sum: Set[Tuple[int]] = set()

        # 🔁 Two Pointer based 2Sum
        # Finds all pairs in nums[start_Index ... end_Index]
        # such that their sum = required_Sum
        def two_Sum(required_Sum: int, start_Index: int, end_Index: int) -> List[List[int]]:
            
            # 🎯 Store unique pairs
            pairs_With_Required_Sum: Set[int] = set()

            # 👈👉 Initialize two pointers
            while start_Index < end_Index:

                # ➕ Current sum of two elements
                current_Sum: int = nums[start_Index] + nums[end_Index]

                # 🎯 Case 1: Found valid pair
                if current_Sum == required_Sum:

                    # 📥 Add pair to set (avoids duplicates)
                    pairs_With_Required_Sum.add(
                        tuple([nums[start_Index], nums[end_Index]])
                    )

                    # 🔄 Move both pointers inward
                    start_Index += 1
                    end_Index -= 1

                # ⬆️ Case 2: Sum too large → decrease it
                elif current_Sum > required_Sum:
                    end_Index -= 1

                # ⬇️ Case 3: Sum too small → increase it
                else:
                    start_Index += 1

            # 🔄 Convert set → list of lists
            return [list(pair) for pair in pairs_With_Required_Sum]

        # 🔄 Sort array (required for two-pointer logic)
        nums.sort()
        n = len(nums)

        # 🔁 Fix first element of triplet
        for i in range(n - 2):

            # 🎯 Now reduce 3Sum → 2Sum
            # Find pairs such that: pair_sum = -nums[i]
            required_Sum: int = 0 - nums[i]

            pairs_With_Required_Sum: List[int] = two_Sum(
                required_Sum = required_Sum, 
                start_Index = i + 1,   # ensure different indices
                end_Index = n - 1
            )

            # ✅ If valid pairs found
            if len(pairs_With_Required_Sum) > 0:

                # 🔁 Form triplets
                for pair in pairs_With_Required_Sum:

                    # ➕ Add fixed element to pair
                    pair.append(nums[i])

                    # 🔄 Sort for consistent ordering
                    # 📥 Add to set to ensure uniqueness
                    triplets_With_Zero_Sum.add(
                        tuple(sorted(pair))
                    )

        # 🔄 Convert set → list of lists
        return [list(triplet) for triplet in triplets_With_Zero_Sum]