def calculator(remaining, denomination, coins_dict):
    
    while remaining >= denomination:
        coins_dict[denomination] += 1
        remaining -= denomination
        
    return remaining
        
remaining = int(100 * float(input("Input the number of dollars you want to carry: ")))

quarter = 25
dime = 10
nickel = 5
penny = 1

#num_coins[quarter] -> 4

num_coins = {
    quarter: 0,
    dime: 0,
    nickel: 0,
    penny: 0
}

#num_coins[denomination] += 1

remaining = calculator(remaining, quarter, num_coins)
print("You have {} quarters with {} cents remaining!".format(num_coins[quarter], remaining))
remaining = calculator(remaining, dime, num_coins)
print("You have {} dimes with {} cents remaining!".format(num_coins[dime], remaining))
remaining = calculator(remaining, nickel, num_coins)
print("You have {} nickels with {} cents remaining!".format(num_coins[nickel], remaining))
remaining = calculator(remaining, penny, num_coins)
print("You have {} pennies with {} cents remaining!".format(num_coins[penny], remaining))
