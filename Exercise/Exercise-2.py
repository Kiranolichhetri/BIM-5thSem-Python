# create a python program capable of greeting you with good morning,
# good afternoo and good evening. your program should use the Module
# to get the current hour. 

import time

# Get the current timestamp
timestamp = time.time()

# Convert the timestamp to a string with a specific format
formatted_time = time.strftime("%H:%M:%S", time.localtime(timestamp))

# Determine the greeting based on the current hour
if 5 <= int(time.strftime("%H", time.localtime(timestamp))) < 12:
    greeting = "Good Morning"
elif 12 <= int(time.strftime("%H", time.localtime(timestamp))) < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

# Print the greeting with the formatted time
print(f"{greeting}! The current time is {formatted_time}.")
