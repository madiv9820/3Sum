from typing import List, Set, Tuple

class pySolution:
    def py_threeSum(self, nums: List[int]) -> List[List[int]]:
        # 🎯 Set to store UNIQUE triplets (as tuples)
        # Using a set automatically removes duplicates 🚫
        triplets_With_Zero_Sum: Set[Tuple[int]] = set()

        # 📏 Length of the input array
        n = len(nums)
        
        # 🔁 First loop: pick the first element of the triplet
        for i in range(n - 2):
            
            # 🔁 Second loop: pick the second element (after i)
            for j in range(i + 1, n - 1):
                
                # 🔁 Third loop: pick the third element (after j)
                for k in range(j + 1, n):
                    
                    # ➕ Check if the sum of the three elements is ZERO ⚖️
                    if nums[i] + nums[j] + nums[k] == 0:
                        
                        # 🔄 Sort the triplet to maintain a consistent order
                        # This ensures permutations like (1, -1, 0) and (-1, 0, 1)
                        # are treated as the SAME triplet 🔁
                        sorted_triplet = tuple(sorted([
                            nums[i], nums[j], nums[k]
                        ]))
                        
                        # 📥 Add the triplet to the set (duplicates automatically ignored ✅)
                        triplets_With_Zero_Sum.add(sorted_triplet)

        # 🔄 Convert the set of tuples into a list of lists for the final result
        return [list(triplet) for triplet in triplets_With_Zero_Sum]