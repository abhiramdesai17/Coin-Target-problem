class Coin:
    def coins(self, coins):
        """
        """
        self.coins = sorted(coins, reverse=True)  # Sort coins in descending order, iterate starting from coin with highest denomination

    def value(self, value):

        # Initializing a dictionary to store the number of each coin used to make up the value
        used = {}

        # Iterating through the sorted coin denominations
        for coin in self.coins:
            
            # Condition to check if the the current coin can be used to make up the target value
            if value >= coin:
                
                # Calculate how many coins of this denomination are needed
                count = value // coin   # Integer division gives the number of coins needed

                # Store the count of this coin in the 'used' dictionary
                used[coin] = count    # Modulo gives the remaining value after using the coins
                
                 # Update the value by subtracting the total covered by this coin
                value %= coin 

                # If value becomes 0, we can stop as we've made the exact amount
                if value == 0:
                    break

        return used


# Example Usage of Greedy Solution
coins = [1, 5, 11]
target = 15

# Create an instance of the CoinsGreedy class
coin1 = Coin()
coin1.coins(coins)

# Get the result for the given target using greedy approach
output = coin1.value(target)
print("Output:", output)


# Explanation of why Greedy Approach is incorrect in this case:
#
#  In this case, the greedy approach chooses the largest denomination (11) first and subtracts it from the target (15).
#  This leaves us with 4. The greedy approach now chooses the largest coin smaller than 4, which is 1.
#  It then selects 1 coin of denomination 1 four times, resulting in the solution {11: 1, 1: 4}.
#  The greedy approach gives a result of 5 coins: 1 coin of denomination 11 and 4 coins of denomination 1.
#
# Why This Doesn't Work:
# 
# 1. The greedy approach doesn't always find the minimum number of coins, because it only looks for the best option at each step, 
#    without considering the overall optimal solution.
# 2. In this case, the optimal solution (which can be found using Dynamic Programming) would be 3 coins: 
#    3 coins of 5. This would result in a total of 3 coins, rather than 5.
# 3. Greedy fails to see that using three 5 coins would minimize the total number of coins. This is why this approach isn't suitable 
#    for this problem where the denominations are not multiples of each other or not in a structured pattern.

# Conclusion:
# The greedy approach works for problems where coin denominations are structured in a way that larger coins are always optimal 
# at each step. But in cases like this, where the denominations are not multiples of each other (e.g., 1, 5, 11), the greedy 
# approach can lead to suboptimal results.
