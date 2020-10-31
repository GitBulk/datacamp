'''
INTRODUCTION:
Comparing language conversion rate (II)
Next, you want to look at the conversion rate by the language that the marketing asset was shown in. While many of your users speak English,
some prefer another language. Let's check to make sure marketing material translated well across languages.

You can analyze metrics by specific demographics using .groupby(). Rather than looking at the overall conversion rate in the dataset, you
instead group by language preference, which allows you to determine whether the marketing campaign was more effective in certain languages.

INTRUCTION:
Group the marketing DataFrame by language_displayed and count the number of unique users in the dataset.
Group marketing by language_displayed again, this time calculating the number of unique users who converted.
Calculate the conversion rate for all languages.
'''

# Group by language_displayed and count unique users
total = marketing.groupby('language_displayed')['user_id'].nunique()

# Group by language_displayed and count unique conversions
subscribers = marketing[marketing['converted'] == True].groupby('language_displayed')['user_id'].nunique()

# Calculate the conversion rate for all languages
language_conversion_rate = subscribers / total
print(language_conversion_rate)
