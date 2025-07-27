# Exercises: Level 1
# Q1 Word Frequency Count
paragraph = """I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the
capabilities to develop an application what else can you love."""

import re
from collections import Counter

words = re.findall(r'\b\w+\b', paragraph.lower())
word_counts = Counter(words)

most_common = word_counts.most_common()
print("Most Frequent Words:", most_common)

most_common = word_counts.most_common(1)
print("Most Frequent Word:", most_common)

# Q2
text = """The position of some particles on the horizontal
x-axis are -12, -4, -3 and -1 in the negative direction,
0 at origin, 4 and 8 in the positive direction."""

import re

numbers = re.findall(r'-?\d+', text)
points = list(map(int, numbers))
sorted_points = sorted(points)
distance = max(points) - min(points)

print("Extracted Points:", points)
print("Sorted Points:", sorted_points)
print("Distance between furthest particles:", distance)

# Exercises: Level 2
import re

def is_valid_variable(var):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, var))

print(is_valid_variable('first_name'))  
print(is_valid_variable('first-name'))  
print(is_valid_variable('1first_name'))  
print(is_valid_variable('firstname'))   

# Exercises: Level 3
import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering
peo@ple.;I found tea@ching m%o@re interesting tha@n any other %jo@bs.
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text) 
    cleaned = re.sub(r'\s+', ' ', cleaned)      
    return cleaned.strip()

cleaned_text = clean_text(sentence)
print(cleaned_text)

def most_frequent_words(text, n=3):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

print(most_frequent_words(cleaned_text))