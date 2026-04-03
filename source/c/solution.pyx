"""
🧩 Cython Wrapper for C 3Sum Implementation

📌 Purpose:
This file acts as a bridge between Python and a C-based implementation
of the 3Sum problem using Cython.

🔍 What this file does:
- 🔗 Connects Python to C function defined in `solution.h`
- 🔄 Converts Python list → C array
- ⚙️ Calls C implementation of 3Sum
- 🔄 Converts C output → Python list of triplets
- 🧹 Frees all dynamically allocated memory to prevent leaks

⚙️ Workflow:
1. Receive Python list input
2. Allocate and populate C array
3. Call C function (`threeSum`)
4. Convert result to Python format
5. Free all allocated memory

🚀 Goal:
Leverage C-level performance ⚡ while maintaining Python usability 🧠
for testing and integration.
"""

from libc.stdlib cimport malloc, calloc, free

# 🔗 Declare external C function from solution.h
cdef extern from 'solution.h':
    int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)


# 🧩 Cython wrapper class for C implementation
cdef class cSolution:

    def c_threeSum(self, nums):
        """
        ⚙️ Python-facing method

        Flow:
        1. Convert Python list → C array 🔄
        2. Call C function ⚡
        3. Convert C result → Python list 🔄
        4. Free all allocated memory 🧹
        """

        # 📏 Step 1: Get input size
        cdef int c_numsSize = len(nums)

        # 🔄 Step 2: Allocate C array (initialized to 0 using calloc)
        cdef int* c_nums = <int*> calloc(c_numsSize, sizeof(int))

        # 📦 Step 3: Allocate return size pointer
        cdef int c_returnSize = 0

        # 📦 Step 4: Declare column sizes pointer (to be set by C function)
        cdef int* c_returnColumnSizes = NULL

        # 🔄 Step 5: Copy Python list → C array
        for i in range(len(nums)):
            c_nums[i] = nums[i]

        # ⚙️ Step 6: Call C function
        # - nums → input array
        # - numsSize → size of array
        # - returnSize → pointer to store number of triplets
        # - returnColumnSizes → pointer to store size of each row
        cdef int** c_result = threeSum(
            c_nums, 
            c_numsSize, 
            &c_returnSize, 
            &c_returnColumnSizes
        )

        # 🔄 Step 7: Convert C result → Python list
        result = []

        if c_result is not NULL:

            # 📊 Iterate through each triplet
            for i in range(c_returnSize):
                result.append([
                    c_result[i][0],
                    c_result[i][1],
                    c_result[i][2]
                ])

            # 🧹 Free column sizes container
            free(c_returnColumnSizes)

            # 🧹 Free result container (outer array)
            free(c_result)

        # 🧹 Step 9: Free input array
        free(c_nums)

        # ✅ Return final Python result
        return result