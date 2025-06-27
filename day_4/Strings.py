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

#Question 18
PFE = "Python for Everyone"

#Question 19
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
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])  

#Question 25
print(sentence.find('because')) 

#Question 26
print(sentence[start:end])  

#Question 27
print("Coding For All".startswith('Coding'))  

#Question 28
print("Coding For All".endswith('coding')) 

#Question 29

