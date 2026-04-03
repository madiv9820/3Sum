# [🧩 3Sum — Find All Unique Triplets](https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150)

### 📖 Problem Statement

You are given an integer array **`nums`**. Your task is to find **all unique triplets** in the array such that:

👉 The sum of the three numbers is equal to zero <br>
👉 **`nums[i] + nums[j] + nums[k] == 0`**

### 🎯 Objective

Return all distinct triplets **`[nums[i], nums[j], nums[k]]`** that satisfy the condition.

#### ⚠️ Important Conditions
- 📍 All indices must be **different** <br>
→ **`i ≠ j`**, **`i ≠ k`**, **`j ≠ k`**
- 🚫 The result must **not contain duplicate triplets**
- 🔄 The **order of elements inside a triplet does not matter**
- 🔀 The **order of triplets in the output does not matter**

### 📌 Examples

#### 🔹 Example 1

- **Input:**
    ```
    nums = [-1, 0, 1, 2, -1, -4]
    ```

- **Output:**
    ```
    [[-1, -1, 2], [-1, 0, 1]]
    ```

- **Explanation:**

    The valid triplets that sum to zero are:
    - [-1, 0, 1]
    - [-1, -1, 2]

#### 🔹 Example 2

- **Input:**
    ```
    nums = [0, 1, 1]
    ```

- **Output:**
    ```
    []
    ```

- **Explanation:** <br>

    No combination of three numbers results in a sum of zero.

#### 🔹 Example 3

- **Input:**
    ```
    nums = [0, 0, 0]
    ```

- **Output:**
    ```
    [[0, 0, 0]]
    ```

- **Explanation:**

    The only possible triplet sums to zero.

### 🔒 Constraints
- 📏 **`3 <= nums.length <= 3000`**
- 🔢 **`-10⁵ <= nums[i] <= 10⁵`**

### 🧾 Summary
- You are given an integer array
- You must return **all unique triplets**
- Each triplet must sum to **zero**
- The result must contain **no duplicates**

---