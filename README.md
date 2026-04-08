# 🧩 3Sum Problem — Brute Force Approach

### 💡 Intuition (How to Think About It) 🧠
At its core, this problem is about:
    
🔍 Finding **all combinations of 3 elements** whose sum equals zero

The most straightforward idea is:
- If we need **3 elements**, we can:
    - Fix the first element
    - Try all possible second elements
    - Try all possible third elements

👉 This naturally leads to **three nested loops** 🔁🔁🔁

#### ⚠️ Duplicate Problem

Different orders of the same numbers can create duplicate triplets:

```
(-1, 0, 1) and (0, -1, 1)
```

To handle this:
- 🔄 Always **sort each triplet**
- 📥 Store results in a set to ensure uniqueness

### 🛠️ Approach: Brute Force

- Generate all possible triplets
- Check if their sum is zero
- Store only unique ones

### 🧾 Pseudocode

```
Initialize an empty set to store unique triplets

Let n = length of nums

For i from 0 to n-3:
    For j from i+1 to n-2:
        For k from j+1 to n-1:

            If nums[i] + nums[j] + nums[k] == 0:

                Create a triplet [nums[i], nums[j], nums[k]]

                Sort the triplet

                Convert it into a tuple (so it can be stored in a set)

                Add it to the set

Convert the set into a list of lists

Return the result
```

### 🧠 Key Insights

- **🔁 Three loops** → explore all combinations
- **🔄 Sorting triplets** → ensures consistency
- **📥 Set usage** → removes duplicates automatically

### ⏱️ Complexity Analysis

| **Type**     | **Complexity**               |
| -------- | ------------------------ |
| ⏱️ Time  | **`O(n³)`** 🐢               |
| 📦 Space | **`O(k)`** (unique triplets) |

### ⚠️ Limitations

- ❌ Very slow for large inputs
- ❌ Not optimized for interviews
- ❌ Repeats unnecessary work

### 🆚 What’s Next? 🚀

👉 The optimal solution uses:

- Sorting + Two Pointers
- Reduces complexity to **`O(n²)`** ⚡

### 🎯 Summary

- ✔️ Simple and intuitive approach
- ✔️ Great for understanding the problem
- ❌ Not efficient for real-world usage

---