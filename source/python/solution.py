from typing import List, Set, Tuple

class pySolution:
    def py_threeSum(self, nums: List[int]) -> List[List[int]]:
        # 🎯 Set to store UNIQUE triplets (as tuples)
        # Using a set automatically removes duplicates 🚫
        triplets_With_Zero_Sum: Set[Tuple[int]] = set()

        # 🔍 Binary Search Helper Function
        # Searches for required_Element in nums[start_Index ... end_Index]
        def binary_Search(required_Element: int, start_Index: int, end_Index: int) -> bool:
            while start_Index <= end_Index:
                # 📍 Find middle index
                mid_Index = start_Index + (end_Index - start_Index) // 2
                
                # ✅ Element found
                if nums[mid_Index] == required_Element:
                    return True
                
                # ⬅️ Search in left half
                elif nums[mid_Index] > required_Element:
                    end_Index = mid_Index - 1
                
                # ➡️ Search in right half
                else:
                    start_Index = mid_Index + 1
            
            # ❌ Element not found
            return False

        # 🔁 Two Sum using Binary Search
        # Goal: Find all pairs in nums[start_Index ... end_Index]
        # whose sum = required_Sum
        def two_Sum(required_Sum: int, start_Index: int, end_Index: int) -> List[int]:
            pairs_With_Required_Sum = []

            # 🔁 Fix first element of pair
            for i in range(start_Index, end_Index + 1):

                # 🎯 Find second element using binary search
                # Ensures we don't reuse the same index (i + 1)
                if binary_Search(required_Sum - nums[i], i + 1, n - 1):

                    # 🔄 Store sorted pair for consistency
                    pairs_With_Required_Sum.append(
                        sorted([
                            nums[i], 
                            required_Sum - nums[i]
                        ])
                    )

            return pairs_With_Required_Sum
        
        # 🔄 Sort the array (required for binary search)
        nums.sort()
        n: int = len(nums)
        
        # 🔁 Fix first element of triplet
        for i in range(n - 2):

            # 🎯 Find pairs such that pair_sum = -nums[i]
            pairs_With_Required_Sum: List[int] = two_Sum(-nums[i], i + 1, n - 1)

            # ✅ If any valid pairs found
            if len(pairs_With_Required_Sum) > 0:

                # 🔁 Form triplets using current nums[i]
                for pair in pairs_With_Required_Sum:

                    # ➕ Add third element to form triplet
                    pair.append(nums[i])

                    # 🔄 Sort to maintain consistent order
                    # 📥 Add to set to avoid duplicates
                    triplets_With_Zero_Sum.add(tuple(sorted(pair)))

        # 🔄 Convert set → list of lists for final result
        return [list(triplet) for triplet in triplets_With_Zero_Sum]