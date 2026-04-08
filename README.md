# 🧩 3Sum Problem — Two Pointer Approach

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

### 🧾 Pseudocode

```
CREATE an empty set result_set

SORT nums

LET n = length of nums

FUNCTION two_sum(required_sum, left, right):
    CREATE empty set pairs

    WHILE left < right DO
        current_sum = nums[left] + nums[right]

        IF current_sum = required_sum THEN
            ADD (nums[left], nums[right]) to pairs
            left = left + 1
            right = right - 1

        ELSE IF current_sum < required_sum THEN
            left = left + 1

        ELSE
            right = right - 1
        END IF
    END WHILE

    RETURN pairs
END FUNCTION


FOR i = 0 TO n - 3 DO
    required_sum = -nums[i]

    pairs = two_sum(required_sum, i + 1, n - 1)

    FOR each pair in pairs DO
        triplet = pair + nums[i]
        SORT triplet
        ADD triplet to result_set
    END FOR
END FOR

RETURN result_set as list
```

### 🧠 Key Insights

- 🔄 Sorting enables **two-pointer traversal**
- 👈👉 Two pointers reduce search space efficiently
- 🔁 Avoids unnecessary nested loops
- 📥 Set ensures unique triplets

### ⏱️ Complexity Analysis

| **Type**     | **Complexity**               |
| -------- | ------------------------ |
| ⏱️ Time  | **`O(n²)`** 🚀               |
| 📦 Space | **`O(k)`** (unique triplets) |

### ⚠️ Limitations (Current Implementation)

- ❌ Uses extra space (set) for duplicate handling
- ❌ Does not skip duplicates during traversal
- ❌ Slightly less optimal than pure two-pointer version

### 🚀 Next Improvement

👉 Skip duplicates during traversal:
- Skip duplicate **`nums[i]`**
- Skip duplicate **`nums[left]`** and **`nums[right]`**

This removes:
- ❌ Need for set
- 📉 Extra space usage

### 🎯 Summary

- ✔️ Efficient and widely used approach
- ✔️ Reduces complexity to **`O(n²)`**
- ✔️ Uses sorting + two pointers effectively
- ⚠️ Can be further optimized by removing set

---