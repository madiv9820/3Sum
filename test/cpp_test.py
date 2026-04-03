"""
🧪 Test Suite for C++ 3Sum Implementation (via Cython)

📌 Purpose:
This file validates the correctness of the C++ implementation of the 3Sum problem,
accessed through a Cython wrapper (`cppSolution`).

🔍 What this file does:
- 📂 Loads test cases from an external JSON file
- 🔗 Uses Cython to interface with the C++ solution
- ⚙️ Executes the C++ 3Sum logic for each test case
- ✅ Verifies that the output matches expected results
- ⏱️ Ensures performance constraints using timeouts

🧾 Key Features:
- Uses `unittest` for structured and scalable testing
- Uses `subTest` for isolated execution and better debugging
- Handles unordered outputs via normalization before comparison
- Provides clear and custom error messages for failures

⚙️ Workflow:
1. Read test cases from JSON 📂
2. Pass input to C++ implementation via Cython ⚙️
3. Receive computed results from C++ 🔄
4. Normalize and compare with expected output ✅

🚀 Goal:
Ensure the C++ implementation is correct, efficient, and fully compatible
with the Python testing ecosystem.
"""

import os, json, unittest
from typing import List
from timeout_decorator import timeout
from source.cpp.solution import cppSolution

class test_cppSolution(unittest.TestCase):
    def setUp(self):
        """
        🛠️ Setup Method

        Responsibilities:
        - 📂 Load test cases from JSON file
        - 🧠 Initialize solution instance once per test run

        This runs before each test method.
        """

        # 📍 Get absolute path of current test file directory
        currentDirectory = os.path.dirname(os.path.abspath(__file__))

        # 📄 Build path to test cases JSON file
        filePath = os.path.join(currentDirectory, 'cases/cases.json')

        # 📖 Open and load test cases
        with open(filePath, mode="r", encoding="utf-8") as read_file:

            # 🧾 Load all test cases into memory
            self.__testcases = json.load(read_file)

            # 🧠 Initialize solution object (used across all test cases)
            self.__solution = cppSolution()

        # 🔄 Call parent setup (standard practice in unittest)
        return super().setUp()
    
    @timeout(1)  # ⏱️ Enforce time constraint per test (max 1 second)
    def test(self):
        """
        🧪 Main Test Runner

        Flow:
        - Iterate over all test cases 🔁
        - Execute solution for each input ⚙️
        - Validate output against expected result ✅

        Uses subTest for:
        - Better debugging 🔍
        - Isolated failure reporting 📊
        """

        # 🔁 Loop through each test case from JSON
        for testcases in self.__testcases:

            # 🏷️ Extract test case details
            testname: str = testcases['title']                 # Name/title of test case
            nums: List[int] = testcases['input']['nums']       # Input array
            expectedOutput: List[List[int]] = testcases['output']  # Expected list of triplets

            # 🔍 Execute each test case independently
            # Helps identify exactly which test case failed
            with self.subTest(testname):

                # ⚙️ Call the solution method with input
                actualOutput: List[List[int]] = self.__solution.cpp_threeSum(
                    nums=nums
                )

                # 📏 Step 1: Validate number of triplets
                # Ensures:
                # - No missing results ❌
                # - No extra results ❌
                actualLen = len(actualOutput)
                expectedLen = len(expectedOutput)

                if actualLen != expectedLen:
                    self.fail(
                        f'❌ Length Mismatch | Expected = {expectedLen}, Actual = {actualLen}'
                    )

                # 🧹 Step 2: Normalize outputs for comparison
                # Why?
                # - Order of triplets does NOT matter
                # - Order inside each triplet does NOT matter
                #
                # So we:
                # 1. Sort each triplet → [1, -1, 0] → [-1, 0, 1]
                # 2. Sort list of triplets → consistent structure
                normalizedActual = sorted(
                    [sorted(triplet) for triplet in actualOutput]
                )
                normalizedExpected = sorted(
                    [sorted(triplet) for triplet in expectedOutput]
                )

                # ✅ Step 3: Compare normalized outputs
                # If mismatch → fail with detailed message
                if normalizedActual != normalizedExpected:
                    self.fail(
                        f'❌ Value Mismatch\n'
                        f'Expected = {expectedOutput}\n'
                        f'Actual   = {actualOutput}'
                    )

# 🚀 Entry point to execute tests directly
if __name__ == '__main__':
    unittest.main()