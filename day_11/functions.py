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
print(remove_item(food_staff, 'Mango')) 
print(remove_item(numbers, 3))          

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

#LEVEL 2
# Q1 Even and odd numbers
def even_and_odd_numbers(n):
    even_numbers = [i for i in range(n + 1) if i % 2 == 0]
    odd_numbers = [i for i in range(n + 1) if i % 2 != 0]
    return even_numbers, odd_numbers
print(even_and_odd_numbers(100))

# Q2 factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(15))  
print(factorial(10))  

# Q3 check parameter is empty
def is_empty(param):
    if not param:
        return True
    else:
        return False
print(is_empty([]))          
print(is_empty([1, 2, 3]))   

# Q4 statistics of a list
import statistics
def calculate_mean(lst):
    return statistics.mean(lst)

def calculate_median(lst):
    return statistics.median(lst)

def calculate_mode(lst):
    return statistics.mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return statistics.variance(lst)

def calculate_std(lst):
    return statistics.stdev(lst)

#
data = [1, 2, 2, 3, 4, 5, 5, 5]
print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))

#LEVEL 3
# Q1 check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(29))  
print(is_prime(15))  

# Q2 check unique items in a list
def all_unique(lst):
    return len(lst) == len(set(lst))
print(all_unique([1, 2, 3, 4, 5]))
print(all_unique([1, 2, 3, 4, 5, 1]))

# Q3 check same data type
def same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

# 
print(same_type([1, 2, 3]))     
print(same_type([1, '2', 3]))          
print(same_type([]))                     

# Q4 check if a variable is a valid python variable name
import keyword

def is_valid_variable(var):
    if not var.isidentifier():
        return False
    if keyword.iskeyword(var):
        return False
    return True
print(is_valid_variable('my_var'))       

# Q5 
from data.countries_data import countries_data

def most_spoken_languages(n=10):
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

def most_populated_countries(n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return [{'name': country['name'], 'population': country['population']} for country in sorted_countries[:n]]

print("Most Spoken Languages:", most_spoken_languages(10))
print("Most Populated Countries:", most_populated_countries(10))

