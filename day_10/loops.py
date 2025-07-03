#Exercises: Level 1
# Question 1 Iterate from 0 to 10 using a for loop and a while loop
for i in range(11):
    print(i)

j = 0
while j <= 10:
    print(j)
    j += 1

# Question 2 Iterate from 10 to 0 using a for loop and a while loop
for i in range(10, -1, -1):
    print(i)
    
k = 10
while k >= 0:
    print(k)
    k -= 1
    
# Question 3 Print a triangle
for i in range(1, 8):
    print('#' * i)

# Question 4 Using nested loops
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# Question 5 Print multiplication table of 0 to 10
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# Question 6 iterate through the list 
items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in items:
    print(item)

# Question 7 print all even numbers from 0 to 100
for i in range(0, 101, 2):
    print(i)

# Question 8 print all odd numbers from 0 to 100
for i in range(1, 101, 2):
    print(i)


#Exercises: Level 2
# Question 1 sum of all numbers from 0 to 100
sum_all = 0
for i in range(101):
    sum_all += i
print(f"The sum of all numbers is {sum_all}.")

# Question 2 sum of all evens and odds from 0 to 100
sum_even = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odds += i
print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odds}.")


#Exercises: Level 3
# Question 1 iterate through the countries list and print all countries that contain the word 'land'
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
];

land_countries = [country for country in countries if 'land' in country]
print(land_countries)

# Question 2 reversed list of countries
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)

# Question 3 
from countries_data.py import countries_data
from collections import Counter

# 1. Total number of languages
languages = []
for country in countries_data:
    languages.extend(country['languages'])

unique_languages = set(languages)
print("Total number of languages:", len(unique_languages))

# 2. Ten most spoken languages
language_counter = Counter(languages)
most_spoken = language_counter.most_common(10)
print("Top 10 spoken languages:")
for lang, count in most_spoken:
    print(lang, ":", count)

# 3. Ten most populated countries
sorted_by_population = sorted(countries-data, key=lambda x: x['population'], reverse=True)
print("Top 10 most populated countries:")
for country in sorted_by_population[:10]:
    print(country['name'], ":", country['population'])
