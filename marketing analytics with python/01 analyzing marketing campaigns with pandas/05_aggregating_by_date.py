'''
INTRODUCTION:
Aggregating by date
The marketing team wants to know whether there is any difference in the conversion rate based on when in the month, your users saw an ad.
In this exercise, you will practice .groupby() again, this time looking at how metrics have evolved.

INSTRUCTION:
Group the marketing DataFrame by date_served and count the number of unique users per day.
Isolate converted users in marketing while grouping by date_served and counting the number of unique converted users per day.
'''

# Group by date_served and count unique users
total = marketing.groupby('date_served')['user_id'].nunique()

# Group by date_served and count unique converted users
subscribers = marketing[marketing['converted'] == True].groupby('date_served')['user_id'].nunique()

# Calculate the conversion rate per day
daily_conversion_rate = subscribers/total
print(daily_conversion_rate)


