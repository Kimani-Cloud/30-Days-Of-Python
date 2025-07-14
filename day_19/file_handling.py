#Q1
def count_lines_and_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = sum(len(line.split()) for line in lines)
        return len(lines), words

# Example usage:
print(count_lines_and_words('./data/obama_speech.txt'))
print(count_lines_and_words('./data/michelle_obama_speech.txt'))
print(count_lines_and_words('./data/donald_speech.txt'))
print(count_lines_and_words('./data/melina_trump_speech.txt'))

#Q2
import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
        language_counter = Counter()
        for country in countries:
            for language in country.get("languages", []):
                language_counter[language] += 1
        return language_counter.most_common(top_n)

# Example usage:
print(most_spoken_languages('./data/countries_data.json', 10))

#Q3
def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
        countries_sorted = sorted(countries, key=lambda c: c['population'], reverse=True)
        return [{'country': c['name'], 'population': c['population']} for c in countries_sorted[:top_n]]

# Example usage:
print(most_populated_countries('./data/countries_data.json', 10))

#Q4
import re

def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', content)

# Example usage:
emails = extract_emails('./data/email_exchange_big.txt')
print(emails[:10])  # preview first 10

#Q5
from collections import Counter
import re

def find_most_common_words(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().lower()
        words = re.findall(r'\b\w+\b', content)
        return Counter(words).most_common(top_n)

# Example usage:
print(find_most_common_words('sample.txt', 10))

#Q6
# Reuse the function above
print(find_most_common_words('./data/obama_speech.txt', 10))
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))
print(find_most_common_words('./data/donald_speech.txt', 10))
print(find_most_common_words('./data/melina_trump_speech.txt', 10))

#Q7
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def remove_support_words(words, stopwords):
    return [word for word in words if word not in stopwords]

def check_text_similarity(file1, file2, stopwords_file='./data/stop_words.txt'):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = clean_text(f1.read())
        text2 = clean_text(f2.read())

    with open(stopwords_file, 'r') as swf:
        stopwords = set(swf.read().split())

    words1 = remove_support_words(text1.split(), stopwords)
    words2 = remove_support_words(text2.split(), stopwords)

    common = set(words1) & set(words2)
    similarity = len(common) / ((len(set(words1)) + len(set(words2))) / 2) * 100

    return round(similarity, 2)

# Example usage:
print(check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt'))

#Q8
print(find_most_common_words('./data/romeo_and_juliet.txt', 10))

#Q9
def count_lines_with_keywords(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    python_count = sum(1 for line in lines if 'python' in line.lower())
    js_count = sum(1 for line in lines if 'javascript' in line.lower())
    java_only_count = sum(1 for line in lines if 'java' in line.lower() and 'javascript' not in line.lower())
    
    return python_count, js_count, java_only_count

# Example usage:
print(count_lines_with_keywords('./data/hacker_news.csv'))

#END