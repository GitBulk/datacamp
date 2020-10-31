'''
INTRODUCTION:
Calculating conversion rate
In this exercise, you will practice calculating conversion rate, which is often the first metric you'll want to calculate
when evaluating how a marketing campaign performed.

On marketing teams, conversion rate is typically the most important metric. It is one of the best ways to determine how
effective a marketing team was at gaining new customers.

As a reminder, conversion rate is the percentage of the users who saw our marketing assets and subsequently became subscribers.

The formula for conversion rate is:

N = Number of people who convert / Total number of people who we market to


INTRUCTION:
Calculate the number of unique user_ids in marketing DataFrame.
Calculate the number of people who subscribed using the converted column.
Calculate the conversion rate.
'''

# Calculate the number of people we marketed to
total = marketing['user_id'].nunique()

# Calculate the number of people who subscribed
subscribers = marketing[marketing['converted'] == True]['user_id'].nunique()

# Calculate the conversion rate
conversion_rate = subscribers / total
print(round(conversion_rate*100, 2), "%")
