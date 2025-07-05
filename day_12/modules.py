#leve1 1
# question 1
import random
import string

def random_user_id():
    """Generates a six-character random user ID."""
    characters = string.ascii_letters + string.digits # All letters (upper and lower) and digits
    return ''.join(random.choice(characters) for _ in range(6))

print(random_user_id())

#question 2
import random
import string

def user_id_gen_by_user():
    """
    Generates user IDs based on user input for character length and number of IDs.
    """
    try:
        num_chars = int(input("Enter the number of characters for each ID: "))
        num_ids = int(input("Enter the number of IDs to generate: "))
    except ValueError:
        return "Invalid input. Please enter integers for both values."

    if num_chars <= 0 or num_ids <= 0:
        return "Number of characters and IDs must be positive integers."

    characters = string.ascii_letters + string.digits
    generated_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        generated_ids.append(user_id)
    return '\n'.join(generated_ids)
print(user_id_gen_by_user())



# question 3

def rgb_color_gen():
    """Generates a random RGB color string."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())


# level 2

#question 1

import random

def list_of_hexa_colors(num_colors):
    """
    Returns a list of 'num_colors' random hexadecimal color codes.
    Each color is in the format '#RRGGBB'.
    """
    hex_colors = []
    for _ in range(num_colors):
        # Generate a random integer between 0 and 0xFFFFFF (16777215)
        # and format it as a 6-digit hexadecimal string, padded with leading zeros if necessary.
        hex_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        hex_colors.append(hex_color)
    return hex_colors 
print(list_of_hexa_colors(3)) 
print(list_of_hexa_colors(1))


# question 2

import random

def list_of_rgb_colors(num_colors):
    """
    Returns a list of 'num_colors' random RGB color strings.
    Each color is in the format 'rgb(R, G, B)'.
    """
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r}, {g}, {b})")
    return rgb_colors

print(list_of_rgb_colors(3)) 
print(list_of_rgb_colors(1)) 


#question 3
def generate_colors(color_type, num_colors):
    """
    Generates a list of random colors, either hexadecimal or RGB, based on input.

    Args:
        color_type (str): 'hexa' for hexadecimal colors or 'rgb' for RGB colors.
        num_colors (int): The number of colors to generate.

    Returns:
        list: A list of generated color strings.
    """
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."

# Example usage:
print(generate_colors('hexa', 3)) 
print(generate_colors('hexa', 1)) 
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))


#level 3

#question 1

import random

def shuffle_list(input_list):
    """
    Takes a list as a parameter and returns a new shuffled list.
    The original list remains unchanged.
    """
    shuffled_copy = list(input_list) 
    random.shuffle(shuffled_copy)   
    return shuffled_copy

my_original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffled = shuffle_list(my_original_list)
print(f"Original list: {my_original_list}")
print(f"Shuffled list: {shuffled}")

#question 3

import random

def unique_seven_numbers():
    """
    Returns a list of seven unique random numbers in the range of 0-9.
    """
    
    if 7 > 10: 
        return "Cannot generate 7 unique numbers in the range 0-9 as there are only 10 unique numbers available."
    
    return random.sample(range(10), 7)

print(unique_seven_numbers())
