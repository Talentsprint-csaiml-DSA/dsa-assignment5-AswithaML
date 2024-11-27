def min_coins(coins, target_amount):
    # Initialize dp array with infinity for all amounts except 0
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0
    
    # Iterate over each amount from 1 to target_amount
    for amount in range(1, target_amount + 1):
        # Check each coin denomination
        for coin in coins:
            if amount - coin >= 0:  # If the coin can be used for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return the result for the target amount
    return dp[target_amount] if dp[target_amount] != float('inf') else -1

# Example usage
coins = [1, 4, 6, 9, 14]
target_amount = 26
result = min_coins(coins, target_amount)
print(f"The minimum number of coins needed to make {target_amount} is: {result}")

