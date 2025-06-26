import math

# Declare variables
my_age = 22  
my_height = 1.49 
my_complex_number = 3 + 4j  

print(f"My age: {my_age} (Type: {type(my_age)})")
print(f"My height: {my_height} (Type: {type(my_height)})")
print(f"My complex number: {my_complex_number} (Type: {type(my_complex_number)})")
print("-" * 30)

# Calculate area of a triangle
print("Calculating the area of a triangle:")
try:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area_triangle = 0.5 * base * height
    print(f"The area of the triangle is {area_triangle}")
except ValueError:
    print("Invalid input. Please enter numbers for base and height.")
print("-" * 30)

# Calculate perimeter of a triangle
print("Calculating the perimeter of a triangle:")
try:
    side_a = int(input("Enter side a: "))
    side_b = int(input("Enter side b: "))
    side_c = int(input("Enter side c: "))
    perimeter_triangle = side_a + side_b + side_c
    print(f"The perimeter of the triangle is {perimeter_triangle}")
except ValueError:
    print("Invalid input. Please enter numbers for triangle sides.")
print("-" )

# Calculate area and perimeter of a rectangle
print("Calculating the area and perimeter of a rectangle:")
try:
    length_rect = int(input("Enter length of the rectangle: "))
    width_rect = int(input("Enter width of the rectangle: "))
    area_rectangle = length_rect * width_rect
    perimeter_rectangle = 2 * (length_rect + width_rect)
    print(f"The area of the rectangle is {area_rectangle}")
    print(f"The perimeter of the rectangle is {perimeter_rectangle}")
except ValueError:
    print("Invalid input. Please enter numbers for length and width.")
print("-" * 30)

# Calculate area and circumference of a circle
print("Calculating the area and circumference of a circle:")
PI = 3.14
try:
    radius_circle = float(input("Enter radius of the circle: "))
    area_circle = PI * radius_circle * radius_circle
    circumference_circle = 2 * PI * radius_circle
    print(f"The area of the circle is {area_circle}")
    print(f"The circumference of the circle is {circumference_circle}")
except ValueError:
    print("Invalid input. Please enter a number for the radius.")
print("-" * 30)

# Calculate slope, x-intercept, y-intercept of y = 2x - 2
print("Analyzing the line y = 2x - 2:")
# The equation is in the form y = mx + c, where m is the slope and c is the y-intercept.
slope_line1 = 2
y_intercept_line1 = -2
# To find the x-intercept, set y = 0 and solve for x:
# 0 = 2x - 2
# 2x = 2
# x = 1
x_intercept_line1 = 1
print(f"The slope of y = 2x - 2 is: {slope_line1}")
print(f"The y-intercept of y = 2x - 2 is: {y_intercept_line1}")
print(f"The x-intercept of y = 2x - 2 is: {x_intercept_line1}")
print("-" * 30)

# Find slope and Euclidean distance between point (2, 2) and point (6, 10)
print("Analyzing points (2, 2) and (6, 10):")
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate slope (m = (y2 - y1) / (x2 - x1))
if x2 - x1 != 0:
    slope_points = (y2 - y1) / (x2 - x1)
    print(f"The slope between ({x1}, {y1}) and ({x2}, {y2}) is: {slope_points}")
else:
    slope_points = "undefined (vertical line)"
    print(f"The slope between ({x1}, {y1}) and ({x2}, {y2}) is: {slope_points}")


# Calculate Euclidean distance (sqrt((x2 - x1)^2 + (y2 - y1)^2))
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {euclidean_distance}")
print("-" * 30)

# Compare the slopes in tasks 6 and 7
print("Comparing slopes from Task 6 and Task 7:")
# Ensure slope_points is a number for comparison
if isinstance(slope_points, (int, float)):
    if slope_line1 == slope_points:
        print(f"The slope from Task 6 ({slope_line1}) is equal to the slope from Task 7 ({slope_points}).")
    else:
        print(f"The slope from Task 6 ({slope_line1}) is NOT equal to the slope from Task 7 ({slope_points}).")
else:
    print(f"The slope from Task 7 is {slope_points}, so it cannot be directly compared to the slope from Task 6.")
print("-" * 30)

# Calculate y = x^2 + 6x + 9 and find x when y is 0
print("Analyzing the quadratic equation y = x^2 + 6x + 9:")
# This is a perfect square trinomial: (x + 3)^2
# To find when y = 0, we set (x + 3)^2 = 0, which means x + 3 = 0, so x = -3.
test_x_values = [-5, -4, -3, -2, -1, 0]
for x_val in test_x_values:
    y_val = x_val**2 + 6 * x_val + 9
    print(f"For x = {x_val}, y = {y_val}")

print("From the calculations, y is 0 when x = -3.")
print("-" * 30)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("Comparing lengths of 'python' and 'dragon':")
len_python = len('python')
len_dragon = len('dragon')
print(f"Length of 'python': {len_python}")
print(f"Length of 'dragon': {len_dragon}")
falsy_comparison = (len_python != len_dragon) # Both are 6, so 6 != 6 is False
print(f"Falsy comparison (len('python') != len('dragon')): {falsy_comparison}")
print("-" * 30)

# Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print("Checking for 'on' in 'python' and 'dragon':")
check_on_in_both = ('on' in 'python') and ('on' in 'dragon')
print(f"'on' is found in both 'python' and 'dragon': {check_on_in_both}")
print("-" * 30)

# Use 'in' operator to check if 'jargon' is in the sentence.
sentence = "I hope this course is not full of jargon."
print(f"Checking for 'jargon' in the sentence: '{sentence}'")
check_jargon_in_sentence = 'jargon' in sentence
print(f"'jargon' is in the sentence: {check_jargon_in_sentence}")
print("-" * 30)

#  There is no 'on' in both dragon and python (falsy statement provided)
# This task asks to verify the statement "There is no 'on' in both dragon and python".
# We already know from Task 11 that 'on' *is* in both, so this statement is False.
print("Verifying the statement: 'There is no 'on' in both dragon and python'")
statement_truth = ('on' not in 'dragon') and ('on' not in 'python')
print(f"The statement is: {statement_truth}") # This will correctly print False
print("-" * 30)

# Find the length of the text 'python' and convert the value to float and convert it to string
print("Converting length of 'python':")
text = 'python'
length_text = len(text)
print(f"Length of '{text}': {length_text} (Type: {type(length_text)})")

float_length = float(length_text)
print(f"Length as float: {float_length} (Type: {type(float_length)})")

string_float_length = str(float_length)
print(f"Length as string after float conversion: {string_float_length} (Type: {type(string_float_length)})")
print("-" * 30)

# How to check if a number is even or not using python?
print("Checking if a number is even:")
number_to_check = 14
is_even = (number_to_check % 2 == 0)
print(f"Is {number_to_check} an even number? {is_even}")

number_to_check = 7
is_even = (number_to_check % 2 == 0)
print(f"Is {number_to_check} an even number? {is_even}")
print("-" * 30)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Comparing floor division and int conversion:")
floor_div_result = 7 // 3
int_converted_value = int(2.7)
comparison_result = (floor_div_result == int_converted_value)
print(f"Floor division of 7 by 3 ({floor_div_result}) == int converted value of 2.7 ({int_converted_value})? {comparison_result}")
print("-" * 30)

# Check if type of '10' is equal to type of 10
print("Comparing types of '10' and 10:")
type_str_10 = type('10')
type_int_10 = type(10)
type_comparison = (type_str_10 == type_int_10)
print(f"Type of '10' ({type_str_10}) == Type of 10 ({type_int_10})? {type_comparison}")
print("-" * 30)

# Check if int('9.8') is equal to 10
print("Checking int('9.8') vs 10:")
try:
    int_9_8 = int('9.8')
    comparison_int_9_8 = (int_9_8 == 10)
    print(f"int('9.8') ({int_9_8}) == 10? {comparison_int_9_8}")
except ValueError as e:
    print(f"Cannot convert '9.8' to an integer: {e}. Therefore, comparison cannot be made.")
print("-" * 30)

# Calculate weekly earning
print("Calculating weekly earning:")
try:
    hours = float(input("Enter hours: "))
    rate_per_hour = float(input("Enter rate per hour: "))
    weekly_earning = hours * rate_per_hour
    print(f"Your weekly earning is {weekly_earning}")
except ValueError:
    print("Invalid input. Please enter numbers for hours and rate.")
print("-" * 30)

# Calculate the number of seconds a person can live
print("Calculating seconds lived:")
try:
    years_lived = int(input("Enter number of years you have lived: "))
    # Assuming 100 years as the maximum lifespan for calculation
    # Or, if the user input is intended to be the total years they will live, use that.
    # The prompt says "Assume a person can live hundred years" and then "Enter number of years you have lived: 100"
    # This implies calculating seconds for the *entered* years, not *up to* 100 if they lived less.
    seconds_in_a_year = 365 * 24 * 60 * 60
    total_seconds_lived = years_lived * seconds_in_a_year
    print(f"You have lived for {int(total_seconds_lived)} seconds.")
except ValueError:
    print("Invalid input. Please enter a number for years.")
print("-" * 30)

# Display the following table
print("Displaying table:")
print("Number  1^0  Number  Number^2  Number^3")
for i in range(1, 6):
    # i^0 is always 1 for any non-zero number, here represented as '1' based on the example.
    # The second column in the example is always '1', which suggests 1^0 not i^0.
    # Let's follow the example output strictly:
    # 1 1 1 1 1
    # 2 1 2 4 8
    # 3 1 3 9 27
    # 4 1 4 16 64
    # 5 1 5 25 125
    # This implies the second column is fixed at 1, then the number itself, then square, then cube.
    print(f"{i:<7} {1:<4} {i:<7} {i**2:<9} {i**3:<9}")
print("-" * 30)
