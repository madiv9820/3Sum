# 🧩 3Sum Problem — Binary Search Approach

### 💡 Intuition (How to Think About It) 🧠

We know:

🔍 3Sum can be reduced to **2Sum**

**Step-by-step thought process:**
- Fix one element → **`a`**
- Now the problem becomes:

    Find two numbers **`(b, c)`** such that <br>
    **`b + c = -a`**

👉 Instead of checking all pairs (which leads to **`O(n³)`**), we can:

- 🔄 **Sort the array**
- 🔁 Fix two elements (**`a`**, **`b`**)
- 🔍 Use **Binary Search** to find the third element **`c`**

#### 🎯 Key Idea

For every pair **`(a, b)`**, search for **`c = -(a + b)`** using binary search

This reduces unnecessary checks compared to brute force 🚀

### 🛠️ Approach

1. 🔄 Sort the array
2. 🔁 Fix the first element **`a`**
3. 🔁 Find all valid pairs **`(b, c)`** such that:
    - **`b + c = -a`**
4. 🔍 Use **binary search** to find **`c`**
5. 🔄 Sort triplets and store in a set to avoid duplicates
6. 🔚 Convert set → list

### 🧾 Pseudocode

```
CREATE an empty set result_set

SORT nums

LET n = length of nums

FUNCTION binary_search(target, left, right):
    WHILE left <= right DO
        mid = left + (right - left) / 2

        IF nums[mid] == target THEN
            RETURN true
        ELSE IF nums[mid] < target THEN
            left = mid + 1
        ELSE
            right = mid - 1
        END IF
    END WHILE

    RETURN false
END FUNCTION


FUNCTION two_sum(required_sum, start, end):
    CREATE empty list pairs

    FOR i = start TO end DO
        target = required_sum - nums[i]

        IF binary_search(target, i + 1, end) THEN
            pair = [nums[i], target]
            SORT pair
            ADD pair to pairs
        END IF
    END FOR

    RETURN pairs
END FUNCTION


FOR i = 0 TO n - 3 DO
    pairs = two_sum(-nums[i], i + 1, n - 1)

    FOR each pair in pairs DO
        triplet = pair + [nums[i]]
        SORT triplet
        ADD triplet to result_set
    END FOR
END FOR

RETURN result_set as list
```

### 🧠 Key Insights

- 🔄 Sorting enables **binary search**
- 🔁 Reduces 3Sum → 2Sum problem
- 🔍 Binary search avoids scanning entire array
- 📥 Set ensures **unique triplets**

### ⏱️ Complexity Analysis

| **Type**     | **Complexity**               |
| -------- | ------------------------ |
| ⏱️ Time  | **`O(n² log n)`** ⚡          |
| 📦 Space | **`O(k)`** (unique triplets) |

### ⚠️ Limitations
- ❌ Still slower than optimal solution
- ❌ Extra **`log n`** factor due to binary search
- ❌ Generates duplicate pairs (filtered later using set)

### 🚀 Recommended Next Step

👉 Move to **Two Pointer Approach**

- Eliminates binary search
- Handles duplicates efficiently
- Industry-standard interview solution 💯

### 🎯 Summary

- ✔️ Improves over brute force
- ✔️ Uses sorting + binary search effectively
- ❌ Not the most optimal approach
- ✔️ Great intermediate step toward optimal solution

---