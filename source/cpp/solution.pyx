"""
🧩 Cython Wrapper for C++ 3Sum Implementation

📌 Purpose:
This file acts as a bridge between Python and C++ using Cython, allowing
a C++ implementation of the 3Sum problem to be used seamlessly in Python.

🔍 What this file does:
- 🔗 Connects to the C++ `Solution` class defined in `solution.hpp`
- 🔄 Converts Python inputs (List[int]) → C++ vectors (vector<int>)
- ⚙️ Calls the C++ `threeSum` method for computation
- 🔄 Converts C++ output (vector<vector<int>>) → Python lists
- 🧹 Manages memory to prevent leaks

⚙️ Workflow:
1. Receive input from Python
2. Convert input to C++ compatible format
3. Execute high-performance C++ logic
4. Convert result back to Python-friendly format
5. Return result to caller

🚀 Goal:
Leverage C++ performance ⚡ while maintaining Python usability 🧠
for testing, integration, and development.
"""

from libcpp.vector cimport vector

# 🔗 Declare external C++ class and method from solution.hpp
cdef extern from 'solution.hpp':
    cdef cppclass Solution:
        Solution() except +  # 🧠 Constructor (raises exception if fails)
        vector[vector[int]] threeSum(vector[int]& nums)  # 🎯 Target method


# 🧩 Cython wrapper class to bridge Python ↔ C++
cdef class cppSolution:
    cdef Solution* ptr  # 🔹 Pointer to C++ Solution instance

    def __init__(self) -> None:
        """
        🧠 Constructor

        - Allocates memory for C++ Solution object
        - Stores pointer for later use
        """
        self.ptr = new Solution()
    
    def __dealloc__(self) -> None:
        """
        🧹 Destructor

        - Ensures allocated C++ memory is freed
        - Prevents memory leaks
        """
        if self.ptr is not NULL:
            del self.ptr
    
    def cpp_threeSum(self, nums):
        """
        ⚙️ Python-facing method

        Flow:
        1. Convert Python list → C++ vector 🔄
        2. Call C++ threeSum implementation ⚡
        3. Convert result back → Python list 🔄
        """

        # 🔄 Step 1: Convert Python list to C++ vector<int>
        cdef vector[int] cpp_nums
        for i in range(len(nums)):
            cpp_nums.push_back(nums[i])

        # ⚙️ Step 2: Call C++ method
        # NOTE:
        # - Must pass cpp_nums (C++ vector), not Python list
        # - Calls actual C++ logic implemented in solution.hpp/.cpp
        cdef vector[vector[int]] cpp_result = self.ptr.threeSum(cpp_nums)

        # 🔄 Step 3: Convert C++ vector<vector<int>> → Python list
        result = []
        
        cdef int cpp_size = cpp_result.size()

        for i in range(cpp_size):
            # Each inner vector represents a triplet [a, b, c]
            result.append([
                cpp_result[i][0], 
                cpp_result[i][1], 
                cpp_result[i][2]
            ])
        
        # 🧹 Step 4: Free memory of C++ result vector
        # Swap with empty vector to release allocated memory immediately
        vector[vector[int]]().swap(cpp_result)

        # ✅ Return final Python-friendly result
        return result