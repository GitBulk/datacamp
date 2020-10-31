'''
INTRODUCTION:
Comparing language conversion rate (I)
The marketing team wants to determine how effective the campaign was on converting English speakers.

In this exercise, you will isolate the data for English speakers and calculate the conversion rate much like in the previous exercises.
Remember, the formula for conversion rate is:

N = Number of people who convert / Total number of people who we market to


Once you have the conversion rate for English speakers, you can compare it to the overall conversion rate to gain a sense of how effective
the marketing campaign was among this group compared to the overall population.

INTRUCTION:
Using the marketing DataFrame, include only the rows where language_displayed is English.
Calculate the total number of users in the english_speakers DataFrame.
Calculate the number of conversions in the english_speakers DataFrame.
'''

# Isolate english speakers
english_speakers = marketing[marketing['language_displayed'] == 'English']

# Calculate the total number of English speaking users
total = english_speakers.user_id.nunique()

# Calculate the number of English speakers who converted
subscribers = english_speakers[english_speakers['converted'] == True].user_id.nunique()

# Calculate conversion rate
conversion_rate = subscribers/total
print('English speaker conversion rate:', round(conversion_rate*100,2), '%')
