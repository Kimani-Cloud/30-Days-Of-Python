import pandas as pd

# Load the CSV file
df = pd.read_csv('data/hacker_news.csv')

# 1. Get the first five rows
print("First 5 rows:")
print(df.head(), "\n")

# 2. Get the last five rows
print("Last 5 rows:")
print(df.tail(), "\n")

# 3. Get the title column as pandas Series
titles = df['title']
print("Title column as Series:")
print(titles.head(), "\n")  # Displaying only first 5 for brevity

# 4. Count the number of rows and columns
print("Shape of dataset (rows, columns):")
print(df.shape, "\n")

# 5. Filter titles containing 'python' (case-insensitive)
python_titles = df[df['title'].str.contains('python', case=False, na=False)]
print(f"Titles containing 'python': {len(python_titles)} found")
print(python_titles['title'].head(), "\n")

# 6. Filter titles containing 'JavaScript' (case-insensitive)
js_titles = df[df['title'].str.contains('javascript', case=False, na=False)]
print(f"Titles containing 'JavaScript': {len(js_titles)} found")
print(js_titles['title'].head(), "\n")

# 7. Explore the data (basic overview)
print("Dataset Info:")
print(df.info(), "\n")

print("Null Values Per Column:")
print(df.isnull().sum(), "\n")

print("Top 5 Most Frequent Titles:")
print(df['title'].value_counts().head(), "\n")
