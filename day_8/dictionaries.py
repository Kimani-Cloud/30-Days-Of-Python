# Question 1 creating an empty dictionary
dog = {}
print(dog)

# Question 2 adding key-value pairs to the dictionary
dog['name'] = 'Tommy'
dog['color'] = 'Black'
dog['breed'] = 'Mbwa Koko'
dog['legs'] = 4
dog['age'] = 5
print(dog)

# Question 3 creating a student dictionary
student_dict = {
    'first_name': 'Paul',
    'last_name': 'Maina',
    'gender': 'Male',
    'age': 29,
    'marital_status': 'Single',
    'skills': ['Python', 'SQL', 'Streamlit'],
    'country': 'Kenya',
    'city': 'Nairobi',
    'address': {
        'street': 'Moi Avenue',
        'building': 'ABC Towers',
        'postal_code': '00100'
    }
}
print(student_dict)

# Question 4 getting the length of the dictionary
print(len(student_dict))

# Question 5  accessing the skills list
print(student_dict['skills'])
print(student_dict.get('skills'))
print(type(student_dict['skills']))

# Question 6 modifying the skills list
student_dict['skills'].append('GIS')
student_dict['skills'].extend(['Git', 'Statistics'])
print(student_dict['skills'])

# Question 7 get keys as a list
keys_list = list(student_dict.keys())
print(keys_list)

# Question 8 get values as a list
values_list = list(student_dict.values())
print(values_list)

# Question 9 change the dictionary to a list of tuples
items_list = list(student_dict.items())
print(items_list)

# Question 10 delete an item from the dictionary
del student_dict['address']
print(student_dict)

# Question 11 delete dictionary
del dog
print(dog) 
