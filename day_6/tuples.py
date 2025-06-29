# Level 1

# Create an empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Create a tuple containing names of your sisters and your brothers
sisters = ("Mishelly", "Olivia")
brothers = ("Joshua", "Ethan", "Sam")
print(f"Sisters: {sisters}")
print(f"Brothers: {brothers}")

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(f"Siblings: {siblings}")

# How many siblings do you have?
num_siblings = len(siblings)
print(f"Number of siblings: {num_siblings}")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = ("Richard",)
mother = ("Zipporah",)
family_members = siblings + father + mother
print(f"Family members: {family_members}")



# Level 2

# Unpack siblings and parents from family_members

*unpacked_siblings, mother_unpacked, father_unpacked = family_members
print(f"Unpacked siblings: {unpacked_siblings}")
print(f"Unpacked mother: {mother_unpacked}")
print(f"Unpacked father: {father_unpacked}")

# Create fruits, vegetables and animal products tuples.
fruits = ("apple", "banana", "orange", "grape")
vegetables = ("carrot", "broccoli", "spinach", "potato")
animal_products = ("milk", "eggs", "meat", "cheese")
print(f"Fruits: {fruits}")
print(f"Vegetables: {vegetables}")
print(f"Animal products: {animal_products}")

# Join the three tuples and assign it to a variable called food_stuff_tp.
food_stuff_tp = fruits + vegetables + animal_products
print(f"Food stuff tuple: {food_stuff_tp}")

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f"Food stuff list: {food_stuff_lt}")

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle_index_start = (len(food_stuff_tp) - 1) // 2
middle_index_end = len(food_stuff_tp) // 2 + 1 if len(food_stuff_tp) % 2 == 0 else (len(food_stuff_tp) // 2) + 1

middle_items_tp = food_stuff_tp[middle_index_start:middle_index_end]
middle_items_lt = food_stuff_lt[middle_index_start:middle_index_end]
print(f"Middle item(s) from tuple: {middle_items_tp}")
print(f"Middle item(s) from list: {middle_items_lt}")


# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"First three items from list: {first_three}")
print(f"Last three items from list: {last_three}")

# Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp) # This would raise a NameError because it's deleted
print("food_stuff_tp has been deleted.")

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print(f"Is 'Estonia' a nordic country? {is_estonia_nordic}")

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print(f"Is 'Iceland' a nordic country? {is_iceland_nordic}")