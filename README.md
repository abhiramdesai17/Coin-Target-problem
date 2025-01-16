# **Problem Statement**  
Given a set of coin denominations and a target value, find the minimum number of coins required to make the target value. You can use any coin denomination any number of times.  
The solution should return the combination of denominations used and their respective counts.

### **Input**  
- `coins`: A list of integers representing coin denominations (e.g., `[1, 5, 10, 25]`).
- `value`: An integer representing the target value to achieve (e.g., `47`).

### **Output**  
- A dictionary where keys are the coin denominations and values are their counts (e.g., `{25: 1, 10: 2, 1: 2}`).

---

## **Solution Approaches**

### **1. Greedy Algorithm**
- **Description**:  
  The greedy algorithm prioritizes the largest denominations first. It attempts to minimize the number of coins by always using the largest possible coin at each step.
- **Advantages**:  
  - Simple and fast to implement.  
  - Works efficiently for most inputs.  
- **Limitations**:  
  - May fail for specific cases where choosing smaller denominations earlier results in fewer coins overall.  

**Example where it fails**:  
Coins: `[1, 3, 4]`, Value: `6`  
- **Greedy Solution**: `{4: 1, 1: 2}` (3 coins)  
- **Optimal Solution**: `{3: 2}` (2 coins)

---

### **2. Dynamic Programming Algorithm**
- **Description**:  
  The dynamic programming (DP) approach guarantees the minimum number of coins by systematically exploring all possible combinations and building a solution from the bottom up.
- **Advantages**:  
  - Always finds the optimal solution.  
  - Handles all edge cases.  
- **Limitations**:  
  - More complex than the greedy algorithm.  
  - Slightly slower due to additional computation.  

**Example where it succeeds**:  
Coins: `[1, 3, 4]`, Value: `6`  
- **Optimal Solution**: `{3: 2}` (2 coins)

