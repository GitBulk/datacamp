'''
INTRODUCTION:
Creating daily conversion rate DataFrame
To understand trends over time, you will create a new DataFrame that includes the conversion rate each day. You will follow essentially the same steps as before
when you calculated the overall conversion rate, this time also grouping by the date a user subscribed.

Looking at the daily conversion rate is crucial to contextualize whether the conversion rate on a particular day was good or bad. Additionally, looking at
conversion rate over time can help to surface trends such as a conversion rate that appears to be going down over time. These kinds of trends are crucial to
identify for your marketing stakeholders as early as possible.


INTRUCTION:
Group marketing by 'date_served' and calculate the unique number of user IDs.
Select only the rows in marketing where converted equals True. Group the result by 'date_served' and calculate the unique number of user IDs.
'''

# Group by date_served and count unique users
total = marketing.groupby('date_served')['user_id'].nunique()

# Group by date_served and calculate subscribers
subscribers = marketing[marketing['converted'] == True].groupby('date_served')['user_id'].nunique()

# Calculate the conversion rate for all languages
daily_conversion_rate = subscribers/total
daily_conversion_rate

