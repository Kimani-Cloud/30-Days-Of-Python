#LEVEL 1
# #Question 1
empty_list = []

#Question 2
Languages = ['Gikuyu', 'Dholuo', 'Kalenjin', 'Kikamba', 'Kiswahili', 'Kimaasai', 'Kisii' ]

#Question 3
print(len(Languages))

#Question 4
first_item = Languages[0]
middle_item = Languages[len(Languages) // 2]
last_item = Languages[-1]
print(first_item, middle_item, last_item) 

#Question 5
mixed_data_types = ['Paul Kimani', 29, 1.65, 'Single', 'Nairobi, Kenya']

#Question 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Question 7
print(it_companies)

#Question 8
print(len(it_companies))

#Question 9
print(it_companies[0])  
print(it_companies[len(it_companies) // 2])  
print(it_companies[-1])  

#Question 10
it_companies[1] = 'Samsung'
print(it_companies)

#Question 11
it_companies.append('Intel')
print(it_companies)

#Question 12
it_companies.insert(len(it_companies) // 2, 'Huawei')
print(it_companies)

#Question 13
it_companies[2] = it_companies[2].upper()
print(it_companies)

#Question 14
joined_companies = '#; '.join(it_companies)
print(joined_companies)

#Question 15
print('Oracle' in it_companies) 

#Question 16
it_companies.sort()
print(it_companies)

#Question 17
it_companies.reverse()
print(it_companies)

#Question 18
print(it_companies[:3])

#Question 19
print(it_companies[-3:])

#Question 20
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print(it_companies[mid - 1:mid + 1])
else:
    print(it_companies[mid])

#Question 21
it_companies.pop(0)
print(it_companies)

#Question 22
mid = len(it_companies) // 2
it_companies.pop(mid)
print(it_companies)

#Question 23
it_companies.pop()
print(it_companies)

# Question 24
it_companies.clear()
print(it_companies)

# Question 25
del it_companies

# Question 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
join_list = front_end + back_end
print(join_list)

# Question 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

index = full_stack.index('Redux') + 1
full_stack[index:index] = ['Python', 'SQL']
print(full_stack)


#LEVEL 2
# Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#(a)
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)

#(b)
ages.extend([min_age, max_age])
print( ages)

#(c)
ages.sort() 
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]
print(median_age)

#(d)
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

#(e)
age_range = max_age - min_age
print("Age range:", age_range)

#(f)
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("abs(min - average):", min_diff)
print("abs(max - average):", max_diff)

#(g)
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
  'Colombia',
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
mid_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[mid_index - 1: mid_index + 1]
else:
    middle_countries = [countries[mid_index]]
print("Middle country(ies):", middle_countries)

#(h)
first_half = countries[:(len(countries) + 1) // 2]
second_half = countries[(len(countries) + 1) // 2:]
print("First half:", first_half)
print("Second half:", second_half)

#(i)
named_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = named_countries
print("China:", china)
print("Russia:", russia)
print("USA:", usa)
print("Scandic countries:", scandic_countries)