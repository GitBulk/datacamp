'''
INTRODUCTION:
Setting up conversion indexes
Now that you've determined that language is, in fact, the issue with House Ads conversion, stakeholders need to know how many subscribers
they lost as a result of this bug.

In this exercise, you will index non-English language conversion rates against English conversion rates in the time period before
the language bug arose.

INTRUCTION:
Create a new DataFrame, house_ads_bug, that contains only the rows from house_ads with 'date_served' prior to '2018-01-11'.
Use your conversion_rate() function on the house_ads_bug DataFrame and the 'language_displayed' column.
Using the appropriate row, divide the Spanish, Arabic and German columns of lang_conv by the English column.
'''

# Calculate pre-error conversion rate
house_ads_bug = marketing[marketing['date_served'] < '2018-01-11']
lang_conv = conversion_rate(house_ads_bug, ['language_displayed'])

# Index other language conversion rate against English
spanish_index = lang_conv['Spanish']/lang_conv['English']
arabic_index = lang_conv['Arabic']/lang_conv['English']
german_index = lang_conv['German']/lang_conv['English']

print("Spanish index:", spanish_index)
print("Arabic index:", arabic_index)
print("German index:", german_index)
