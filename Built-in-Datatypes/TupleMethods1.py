countries = ("nepal","india","bangladesh","china","bhutan")

temp = list(countries)

temp.append("pakistan")  #add item in last
temp.pop(3)              #remove item
temp[2] = "maldives"     #change item
countries = tuple(temp)
print(countries)