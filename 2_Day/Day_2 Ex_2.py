# Day 2
# Exercise 2
# 1. Checking data types

print(type("Timi"))
print(type("United Kindom"))
print(type(17))
print(type(False))

# 2. Length of first name

first_name = "Timi"
print(len(first_name))

# 3. Compare the length of your first name and your last name

first_name = "Timi"
last_name = "Ehinmowo"
print("Length of my first name is",len(first_name),"while length of my last name is",len(last_name))

# 4. Performing arithmetic operations using variables

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)

product = num_one*num_two
print(product)

division = num_one/num_two
print(division)

remainder = num_one % num_two
print(remainder)

exp = num_one**num_two
print(exp)

floor_division = num_one//num_two
print(floor_division)


# 5. Area and circumference of a circle with radius of 30m

radius = 30
pi = 22/7
area_of_circle = pi*radius**2
print(area_of_circle)

circum_of_circle = 2*pi*radius
print(circum_of_circle)

# 6. Getting input from user
first_name = input("Enter your first name: ")
print(first_name)
last_name = input("Enter your last name: ")
print(last_name)
country = input("Enter your country: ")
print(country)
age = int(input("Enter your age: "))
print(age)

# 7. Running help('keywords') in Python shell to check for the Python reserved words or keywords

print(help('keywords'))