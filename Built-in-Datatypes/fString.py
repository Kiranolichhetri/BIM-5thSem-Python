
name = input("Enter your name: ")

age = int(input("Enter your age: "))

import time
current_year = int(time.strftime("%Y"))
years_until_100 = 100 - age
year_turn_100 = current_year + years_until_100

print(f"Hello, {name}! You are currently {age} years old.")
print(f"You will turn 100 years old in the year {year_turn_100}.")
