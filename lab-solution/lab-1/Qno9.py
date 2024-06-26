# WAP to create a dictionary that contains districts and their headquarters 
# and then extract the districts for which headquarter names in same as the district name.

# Define a dictionary of districts and their headquarters
districts = {
    "Kathmandu": "Kathmandu",
    "Bhaktapur": "Bhaktapur",
    "Lalitpur": "Lalitpur",
    "Pokhara": "Pokhara",
    "Biratnagar": "Biratnagar",
    "Nepalgunj": "Nepalgunj"
}

# Extract districts where headquarters names are the same as district names
matching_districts = [district for district, hq in districts.items() if district == hq]

# Display the result
print("Districts where headquarters names are the same as district names:")
for district in matching_districts:
    print(district)
