'''
INTRODUCTION:
Setting up our data to visualize daily conversion
When you want to understand how your campaign performed, it is essential to look at how key metrics changed throughout the campaign.
Your key metrics can help you catch problems that may have happened during the campaign, such as a bug in the checkout system that led to
a dip in conversion toward the end of your campaign. Metrics over time can also surface trends like gaining more subscribers over the
weekends or on specific holidays.

In this exercise, you will build upon the daily conversion rate DataFrame daily_conversion_rate you built in a previous exercise. Before
you can begin visualizing, you need to transform your data into an easier format to use with pandas and matplotlib.


INTRUCTION:
Reset the index of daily_conversion_rate and use pd.DataFrame to convert the results into a DataFrame.
Rename the daily_conversion_rate columns to 'date_served' and 'conversion_rate'.
'''

# Reset index to turn the results into a DataFrame
daily_conversion_rate = pd.DataFrame(daily_conversion_rate.reset_index(0))

# Rename columns
daily_conversion_rate.columns = ['date_served', 'conversion_rate']