from cs50 import get_float

coins = 0
# Keep prompting for adequate value
while True:
    dollars = get_float("Change owed: ")
    if dollars > 0:
        break
# Convert to cents
cents = round(dollars * 100)
print(cents)

# Find the least number of coins/steps for change

while (cents >= 25):
    cents -= 25
    coins += 1


while (cents >= 10):
    cents -= 10
    coins += 1


while (cents >= 5):
    cents -= 5
    coins += 1


while (cents >= 1):
    cents -= 1
    coins += 1
    break

# Print the least amount of coins needed for change
print(coins)

