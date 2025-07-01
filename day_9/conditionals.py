# level 1
# question 1
import math
Age = int(input("Enter your Age: "))
#Age = int(Age_str) 

if Age > 18:
    print("You are old enough to drive.")
else:
    print("You need " + str(18 - Age) + " more years to learn to drive.")

    #question 2

My_Age = 22
Your_Age = int(input("Enter your Age.: "))


if Your_Age > My_Age:
    print("You are " +  str(Your_Age - My_Age) + " years older than me.")

else:
    print("You are  " +  str(My_Age - Your_Age) + " years younger than me.")    



#question 3

A = int(input("Enter number one: "))
B = int(input("Enter number two: "))
        
if A > B :
    print(str(A)+ " is greater than "+ str(B))

else:
    print(str(B)+ " is greater than "+ str(A))    


#level 2
# question 1

Grade = int(input("Enter your grade: "))

if 80 <= Grade <= 100:
    print("Your Grade is A")
elif 70 <= Grade <= 79:
    print("Your Grade is B")
elif 60 <= Grade <= 69:
    print("Your Grade is C")
elif 50 <= Grade <= 59:
    print("Your Grade is D")
elif 0 <= Grade <= 49:
    print("Your Grade is F")
else:
    print("Invalid Grade entered. Please enter a grade between 0 and 100.")


#question 2

month = str(input("Enter the Month:"))

if month in ["September", "October" , "November"] :
    print("The Season is Autunm.")

elif month in ["December", "January" , "February"]:
    print("The Season is Winter." )

elif month in ["March", "April" , "May"]:
    print("The Season is Spring.")

elif month in ["June", "July" , "August"]:
    print("The Season is Summer.")

else:
    print ("This is not a valid month." )


#question 3

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits1 =['apple','passion','pinapple']
fruits.extend(fruits1)
print(fruits)

#level 3

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_list = person['skills']
    if len(skills_list) > 0: 
        middle_index = len(skills_list) // 2
        print(f"Middle skill: {skills_list[middle_index]}")

# 2. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

# 3. If a person skills has only JavaScript and React, print('He is a front end developer'),
#    if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#    if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
#    else print('unknown title') - for more accurate results more conditions can be nested!

if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')

# 4. If the person is married and if he lives in Finland, print the information in the following format:
#    Asabeneh Yetayeh lives in Finland. He is married.
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person.get('first_name')} {person.get('last_name')} lives in {person.get('country')}. He is married.")