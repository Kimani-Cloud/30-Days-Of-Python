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




