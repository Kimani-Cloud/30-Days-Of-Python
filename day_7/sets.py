# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#length of the set
len(it_companies)
print(len(it_companies))

#add twitter
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
new_companies = {'Netflix', 'Samsung', 'Sony'}
it_companies.update(new_companies)
print(f"it_companies after adding multiple companies: {it_companies}")

# Remove one of the companies
it_companies.remove('IBM')
print(f"it_companies after removing 'IBM': {it_companies}")

# Difference between remove and discard
#The difference is that remove raises an error if the item isn't found, while discard does nothing if the item isn't found.


#join A and B
C = A.union(B)
print(C)

#Find A intersection B
D = A.intersection(B)
print(D)

#Is A subset of B
E=A.issubset(B)
print(E)  #TRUE

#Are A and B disjoint sets
G=A.isdisjoint(B)
print(G)  # FALSE

#Join A with B and B with A
J=(A.union(B)) .union (B.union(A))
print(J)


#What is the symmetric difference between A and B
K=A.symmetric_difference(B)

print(K)

#Delete the sets completely

del A
del B
del C
del D
del E
del G
del J
del K



#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Age=set(age)
print(Age)

len(age)
len(Age)
if len(age)>len(Age):
    print("list is greater than set")
else:
     print("set is greater than list")


#Explain the difference between the following data types: string, list, tuple and set
#String: Ordered, sequence of characters that can not be changed (text).

#List: Ordered,  collection allowing duplicates and are changeable.(for example; a flexible shopping list).

#Tuple: Ordered, collection allowing duplicates and are not changeable. (for example; fixed coordinates).

#Set: Unordered, collection of unique items and are changeable. ( They remove duplicates automatically).



#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people."

# Convert the sentence to lowercase  and remove the fullstop 
cleaned_sentence = sentence.lower().replace('.', '')

# Split the sentence into a list of words
words = cleaned_sentence.split()

#Convert the list of words into a set to get only unique words
unique_words = set(words)

# Get the count of unique words
num_unique_words = len(unique_words)

print(f"Original sentence: \"{sentence}\"")
print(f"List of all words (after cleaning): {words}")
print(f"Set of unique words: {unique_words}")
print(f"Number of unique words: {num_unique_words}")