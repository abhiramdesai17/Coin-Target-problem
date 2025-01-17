class Coin:
    def coins(self, coins):
        """
        """
        self.coins = coins  # Store the coin denominations in the class

    def value(self, value):
        
        # Create a DP table to store the minimum coins required for each amount
        # dp[i] represents the minimum coins required to achieve amount i

        # Initialize with infinity (unreachable state)
        arr = [float('inf')] * (value + 1)

        # Base case: 0 coins are needed to make the target amount 0
        arr[0] = 0  

        # Create an array to track which coin is used to achieve each amount
        # coin_used[i] will store the coin denomination used to achieve amount i

        # Dictionary to store the coin used to achieve each amount
        used = {}  # Initialize an empty dictionary to track coins used

        # Fill the DP table for all amounts from 1 to the target

        # Iterate through all possible target amounts
        for i in range(1, value + 1):  

            for coin in self.coins:  # Iterate through all available coin denominations

                # Check if the current coin can be used to achieve the current amount t
                if i >= coin and arr[i - coin] + 1 < arr[i]:

                    # Update the minimum coins for amount t
                    arr[i] = arr[i - coin] + 1  
                    used[i] = coin  # Store the coin used to achieve amount t

        # If dp[target] is still infinity, it means the target cannot be achieved
        if arr[value] == float('inf'):
            return {}


        # Backtrack to determine the denominations and their counts
        # Dictionary to store the coins used and their counts
        result = {}  

        # Continue until the value is reduced to 0
        # Loop through the value, reducing it step by step using the coins
        while value > 0:  

            # Get the coin used to achieve the current value
            coin = used[value]  # Retrieve the coin denomination used for the current amount from 'used' dictionary

            # If the coin is already used, increment its count
            if coin in result:  
                result[coin] += 1 # Increment the count of the coin in the result dictionary

            # Otherwise, add the coin to result with a count of 1
            else:  
                result[coin] = 1  # Add the coin with a count of 1 to the result dictionary

            # Reduce the value by the value of the coin used
            value -= coin  

        # Return the result dictionary containing the denominations and their counts
        return result
    
# Example Usage of Backtracking Solution
coins = [1, 5, 11]
target = 15

# Create an instance of the Coin class
coin1 = Coin()
coin1.coins(coins)

# Get the result for the given target using backtracking approach
output = coin1.value(target)
print("Output:", output)


#  Output: {5: 3}
#  Explanation:
#  The 'value' method uses dynamic programming and backtracking to find the minimum coins required
#  to achieve the target amount of 15.
#  In this case, it finds that the optimal solution is to use three coins of denomination 5:
#  5 + 5 + 5 = 15, which is the target amount.
#  Thus, the output is {5: 3}, meaning we use 3 coins of denomination 5 to make the amount 15.
#
#  This approach is better than greedy because it ensures that the solution uses the minimum number of coins.
#  For example, if we used the greedy approach, it would attempt to take one coin of 11 first, 
#  and then use 4 coins of 1, which is suboptimal. The backtracking approach explores all possibilities
#  and returns the optimal solution, ensuring the minimum coins are used.

