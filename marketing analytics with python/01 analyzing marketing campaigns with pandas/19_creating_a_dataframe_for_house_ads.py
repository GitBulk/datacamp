'''
INTRODUCTION:
Creating a DataFrame for house ads
The house ads team is concerned because they've seen their conversion rate drop suddenly in the past few weeks. In the previous exercises,
you confirmed that conversion is down because you noticed a pattern around language preferences.

As a data scientist, it is your job to provide your marketing stakeholders with as specific feedback as possible as to what went wrong
to maximize their ability to correct the problem. It is vital that you not only say "looks like there's a language problem," but instead
identify what the problem is specifically so that the team doesn't repeat their mistake.

INTRUCTION:
Use np.where() to create a new column in house_ads called 'is_correct_lang' whose values are 'Yes' if 'language_displayed' is equal
to 'language_preferred' and 'No' otherwise.
Group by date_served and is_correct_lang to get a daily count of the ads served.
'''
# Add the new column is_correct_lang
house_ads['is_correct_lang'] = np.where(house_ads['language_preferred'] == house_ads['language_displayed'], 'Yes', 'No')

# Groupby date_served and is_correct_lang
language_check = house_ads.groupby(['date_served','is_correct_lang'])['is_correct_lang'].count()

# Unstack language_check and fill missing values with 0's
language_check_df = pd.DataFrame(language_check.unstack(level=1)).fillna(0)

# Print results
print(language_check_df)