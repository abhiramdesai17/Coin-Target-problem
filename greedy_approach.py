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
output_greedy = coin1.value(target)
print("Greedy Approach Output:", output_greedy)
