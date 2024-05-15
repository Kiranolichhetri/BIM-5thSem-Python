#check in list whether even index has odd numbers or not.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22]

found_odd = False

for i in range(0, len(numbers), 2):
    if numbers[i] % 2 != 0:
        print(f"Number at even index {i} ({numbers[i]}) is odd.")
        found_odd = True

if not found_odd:
    print("Even indices do not have odd numbers.")
