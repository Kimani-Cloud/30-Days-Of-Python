# Day 2: 30 Days of python programming

# Declare a first name variable and assign a value to it
first_name = "Marion"

# Declare a last name variable and assign a value to it
last_name = "Minda"

# Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name

# Declare a country variable and assign a value to it
country = "Kenya"

# Declare a city variable and assign a value to it
city = "Nairobi"

# Declare an age variable and assign a value to it
age = 22

# Declare a year variable and assign a value to it
year = 2024

# Declare a variable is_married and assign a value to it
is_married = True

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Declare multiple variables on one line
continent, population, is_capital = "Europe", 5.5, False


# Check the data type of all your variables using type() built-in function
print("--- Data Types ---")
print(f"first_name type: {type(first_name)}")
print(f"last_name type: {type(last_name)}")
print(f"full_name type: {type(full_name)}")
print(f"country type: {type(country)}")
print(f"city type: {type(city)}")
print(f"age type: {type(age)}")
print(f"year type: {type(year)}")
print(f"is_married type: {type(is_married)}")
print(f"is_true type: {type(is_true)}")
print(f"is_light_on type: {type(is_light_on)}")
print(f"continent type: {type(continent)}")
print(f"population type: {type(population)}")
print(f"is_capital type: {type(is_capital)}")
print("------------------\n")


# Using the len() built-in function, find the length of your first name
first_name_len = len(first_name)
print(f"Length of first_name: {first_name_len}")

# Compare the length of your first name and your last name
last_name_len = len(last_name)
print(f"Length of last_name: {last_name_len}")

if first_name_len > last_name_len:
    print("First name is longer than last name.")
elif last_name_len > first_name_len:
    print("Last name is longer than first name.")
else:
    print("First name and last name have the same length.")
print("\n")


# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(f"Total (num_one + num_two): {total}")

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(f"Difference (num_one - num_two): {diff}")

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(f"Product (num_one * num_two): {product}")

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(f"Division (num_one / num_two): {division}")

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print(f"Remainder (num_one % num_two): {remainder}")

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(f"Exponent (num_one ** num_two): {exp}")

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(f"Floor Division (num_one // num_two): {floor_division}")
print("\n")


# The radius of a circle is 30 meters. Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius_fixed = 30
pi = 3.14159
area_of_circle = pi * (radius_fixed ** 2)
print(f"Area of circle (radius={radius_fixed}): {area_of_circle} square meters")

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * radius_fixed
print(f"Circumference of circle (radius={radius_fixed}): {circum_of_circle} meters")
print("\n")


# Take radius as user input and calculate the area.
try:
    radius_input = float(input("Enter the radius of a circle (for user input area calculation): "))
    area_user_input = pi * (radius_input ** 2)
    print(f"Area of circle (user input radius={radius_input}): {area_user_input} square meters")
except ValueError:
    print("Invalid input for radius. Please enter a number.")
print("\n")


# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
print("--- User Input Section ---")
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ") 

print(f"\nUser Entered Details:")
print(f"First Name: {user_first_name}")
print(f"Last Name: {user_last_name}")
print(f"Country: {user_country}")
print(f"Age: {user_age}")
print("------------------------\n")
