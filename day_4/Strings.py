#Question 1 - String Concatenation
w_1 = "Thirty"
w_2 = "Days"
w_3 = "Of"
w_4 = "Python."
Sentence = w_1 + " " + w_2 + " " + w_3 + " " + w_4
print(Sentence)

#Question 2 - String Concatenation 
w_5 = "Coding"
w_6 = "For"
w_7 = "All."
print(w_5 + " " + w_6 + " " + w_7)

#Question 3 and 4
company = "Coding For All"
print(company)

#Question 5 - String Length
print(len(company))

#Question 6 
print(company.upper())

#Question 7
print(company.lower())

#Question 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Question 9 - String Slicing
print(company[0:6]) 

#Question 10 - String finding
print(company.find("Coding"))
print(company.index("Coding"))

#Question 11 - String Replacing
print(company.replace("Coding", "Python"))

#Question 12
print("Python for Everyone".replace("Everyone", "All"))

#Question 13 - String Splitting
print(company.split())

#Question 14 
tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech.split(", ")) 

#Question 15
print(company[0])

#Question 16
print(company[-1])

#Question 17
print(company[10])

#Question 18 acronym
PFE = "Python for Everyone"

#Question 19 acronym
CFA = "Coding For All"

#Question 20 
print(CFA.index('C'))

#Question 21
print(CFA.index('F'))

#Question 22 
print("Coding For All People".rfind('l')) 

#Question 23 
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))  

#Question 24
print(sentence.rindex('because'))  

#Question 25 
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])  

#Question 26
print(sentence.find('because')) 

#Question 27
print(sentence[start:end])  

#Question 28
print("Coding For All".startswith('Coding'))  

#Question 29
print("Coding For All".endswith('coding')) 

#Question 30
print('   Coding For All      '.strip())  

#Question 31
#print("30DaysOfPython".isidentifier())   #False   
print("thirty_days_of_python".isidentifier()) 

#Question 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined = ' # '.join(libraries)
print(joined)

#Question 33 newline escape
print("I am enjoying this challenge.\nI just wonder what is next.")

#Question 34 tab escape
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#Question 35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))  

#Question 36
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
