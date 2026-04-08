# 🧩 3Sum Problem — Space Optimal Two Pointer Approach

### 💡 Intuition (How to Think About It) 🧠

The key idea is:

🔁 Convert **3Sum → 2Sum problem**

Step-by-step thinking:
1. Fix one element **`a`**
2. Now find two numbers **`(b, c)`** such that:
    ```
    b + c = -a
    ```

#### 🚀 Why Two Pointers?

Instead of checking all pairs (brute force ❌), we:
- 🔄 Sort the array
- 👈👉 Use two pointers to efficiently find pairs

### 🎯 Core Logic

After sorting:
- Fix **`a = nums[i]`**
- Initialize:
    - **`left = i + 1`**
    - **`right = n - 1`**

Now:
- ➕ Compute **`current_sum = a + nums[left] + nums[right]`**

#### ⚖️ Decision Making

| Condition             | Action                             |
| --------------------- | ---------------------------------- |
| **`current_sum == 0`** 🎯 | Found triplet → move both pointers |
| **`current_sum < 0`** ⬇️  | Increase sum → move **`left`** ➡️      |
| **`current_sum > 0`** ⬆️  | Decrease sum → move **`right`** ⬅️     |

#### 🔥 Duplicate Handling (Most Important Part)

To ensure **unique triplets**, we skip duplicates **during traversal**:
- 🚫 Skip duplicate values of **`nums[i]`**
- 🚫 After finding a valid triplet:
    - Move **`left`** forward
    - Skip all duplicate values of **`nums[left]`**

👉 This removes the need for a set and keeps space optimal 💯

### 🧾 Pseudocode

```
SORT nums

CREATE empty list result

LET n = length of nums

FOR i = 0 TO n - 3 DO

    IF i > 0 AND nums[i] = nums[i - 1] THEN
        CONTINUE
    END IF

    left = i + 1
    right = n - 1

    WHILE left < right DO

        current_sum = nums[i] + nums[left] + nums[right]

        IF current_sum = 0 THEN

            ADD [nums[i], nums[left], nums[right]] to result

            left = left + 1

            WHILE left < right AND nums[left] = nums[left - 1] DO
                left = left + 1
            END WHILE

        ELSE IF current_sum < 0 THEN
            left = left + 1

        ELSE
            right = right - 1
        END IF

    END WHILE

END FOR

RETURN result
```

### 🧠 Key Insights

- 🔄 Sorting enables efficient pointer movement
- 👈👉 Two pointers reduce search space from **`O(n²)`** → **`O(n)`** per iteration
- 🚫 Duplicate handling during traversal eliminates need for extra space
- ⚡ This is the **most optimal and interview-expected solution**

### ⏱️ Complexity Analysis

| **Type**     | **Complexity**               |
| -------- | ------------------------ |
| ⏱️ Time  | **`O(n²)`** 🚀               |
| 📦 Space | **`O(1)`** (excluding output) 💯 |

### 🎯 Summary

- ✔️ Optimal solution with **`O(n²)`** time
- ✔️ No extra data structures needed
- ✔️ Handles duplicates efficiently
- ✔️ Most commonly expected in interviews

#### 🏁 Final Thought

✨ “Don’t remove duplicates later — avoid creating them in the first place.”

That’s the key to **writing clean and optimal solutions** 💯

---