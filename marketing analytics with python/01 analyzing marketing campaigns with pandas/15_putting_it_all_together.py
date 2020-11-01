'''
INTRODUCTION:
Putting it all together
Your marketing stakeholders have requested a report of the daily conversion rate for each age group, and they need it as soon as possible.
They want you to refresh this report on a monthly cadence. This is a perfect opportunity to utilize your functions. Not only will the
functions help you get this report out promptly today, but it will also help each month when it's time for a refresh of the data.

Remember, conversion_rate() takes a DataFrame and a list of columns to calculate the conversion rate.

INTRUCTION:
Using your conversion_rate() function, create a new DataFrame called age_group_conv which contains conversion rate
by date_served and age_group from the marketing DataFrame.
Unstack age_group_conv to create a DataFrame with each age group as a column. This step has already been done for you.
Use your plotting_conv() function to plot the conversion rates for each age group.
'''

# Calculate conversion rate by date served and age group
age_group_conv = conversion_rate(marketing, ['date_served', 'age_group'])

# Unstack age_group_conv and create a DataFrame
age_group_df = pd.DataFrame(age_group_conv.unstack(level=1))

# Plot the results
plotting_conv(age_group_df)

