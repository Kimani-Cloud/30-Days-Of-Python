# Q1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

# Q2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flattened_list)

# Q3
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

# Q4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [[country.upper(), country[:3].upper(), city.upper()] 
                        for sublist in countries for country, city in sublist]
print(new_list)

# Q5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': country.upper(), 'city': city.upper()} 
        for sublist in countries 
        for (country, city) in sublist]
print(dict_list)

# Q6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [' '.join(name) for sublist in names for name in sublist]
print(full_names)


# Q7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda x, y, m: y - m * x

#
m = slope(1, 2, 3, 6)
b = y_intercept(1, 2, m) if m is not None else None
print(f"Slope: {m}, Intercept: {b}")