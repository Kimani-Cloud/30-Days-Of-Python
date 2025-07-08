from datetime import datetime, date, time, timedelta

# Get the current day, month, year, hour, minute and timestamp
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

print(f"--- Current Datetime Information ---")
print(f"Current Date and Time: {now}")
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")
print(f"Timestamp: {timestamp}")

# Format the current date
t_m_d = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"\n--- Formatted Current Date ---")
print(f"Formatted Date: {t_m_d}")

# Today is 5 December, 2019. Change this time string to time.
# Note: The prompt asks to change 'time string to time'.
# If it meant 'datetime object', then it would be different.
# Assuming it means parsing a string into a datetime object.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(f"\n--- Time String to Datetime Object ---")
print(f"Original string: '{date_string}'")
print(f"Converted datetime object: {date_object}")

# Calculate the time difference between now and new year.
print(f"\n--- Time Difference Calculations ---")
current_year = now.year
next_new_year = datetime(current_year + 1, 1, 1, 0, 0, 0) # January 1st of next year
time_left_for_new_year = next_new_year - now
print(f"Time left for New Year: {time_left_for_new_year}")

# Calculate the time difference between 1 January 1970 and now.
epoch_start = datetime(1970, 1, 1, 0, 0, 0)
time_since_epoch = now - epoch_start
print(f"Time since 1 January 1970: {time_since_epoch}")


# Think, what can you use the datetime module for? Examples:
print(f"\n--- Use Cases for Datetime Module ---")
print("The `datetime` module is incredibly versatile and useful for many applications, including:")
print("1. Time series analysis: Handling and analyzing data points indexed by time.")
print("2. To get a timestamp of any activities in an application: Recording when events occur (e.g., user logins, data modifications).")
print("3. Adding posts on a blog: Stamping articles with their publication date/time.")
print("4. Scheduling tasks: Running specific code at predetermined times.")
print("5. Age calculation: Determining a person's exact age.")
print("6. Event countdowns: Showing time remaining until a specific date.")
print("7. Logging: Recording the time of events in application logs.")
print("8. Data validation: Ensuring dates/times entered by users are valid and in the correct format.")