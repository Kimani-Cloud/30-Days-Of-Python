#Exercises: Level 1
# Q1 sum of two numbers
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(17, 95))

# Q2 calculate the area of a circle
import math
def area_of_circle(r):
    return math.pi * (r ** 2)
print(area_of_circle(14))

# method 2
def area_of_circle(r):
    pi = 3.14
    return pi * r * r
print(area_of_circle(14))

# Q3 
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
            return sum(args)
    else:
            return "All inputs must be numbers."
        
print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, 'z', 4, 5))

# Q4 convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(30))

# Q5 season checker
def check_season(month):
    seasons = {
        'winter': ['December', 'January', 'February'],
        'spring': ['March', 'April', 'May'],
        'summer': ['June', 'July', 'August'],
        'autumn': ['September', 'October', 'November']
    }
    
    for season, months in seasons.items():
        if month in months:
            return season
        else:
            return "Invalid month"
print(check_season('Paul'))
print(check_season('January')) 

# Q6 calculate the slope of a line
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return None
    else:
        return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 6))

# Q7 solve a quadratic equation
#def solve_quadratic(a, b, c):

# Q8
def print_list(lst):
    for item in lst:
        print(item)
        
print_list([1, 2, 3, 'a', 'b'])

# Q9 reverse a list
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['A', 'B', 'C']))

# Q10 capitalize a list
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
print(capitalize_list_items(['gomycode', 'data', 'science']))

# Q11 add item to a list
def add_item(lst, item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# Q12 remove item from a list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# Q13 sum of all numbers in a list
def sum_of_numbers(n):
    return sum(range(n + 1))

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Q14 sum of all odd numbers
def sum_of_odd_numbers(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

print(sum_of_odd_numbers(5)) 

# Q15 sum of all even numbers
def sum_of_even_numbers(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

print(sum_of_even_numbers(5))