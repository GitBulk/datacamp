'''
INTRODUCTION:
Grouping and counting by multiple columns
Stakeholders have begun competing to see whose channel had the best retention rate from the campaign. You must first determine how
many subscribers came from the campaign and how many of those subscribers have stayed on the service.

It's important to identify how each marketing channel is performing because this will affect company strategy going forward. If one channel
is outperforming others, it might signal the channel merits further investment.

You will build on what we have learned about .groupby() in previous exercises, this time grouping by multiple columns.


INTRUCTION:
Use .groupby() to calculate subscribers by subscribing_channel and date_subscribed
'''

channel_age = marketing.groupby(['marketing_channel', 'age_group'])['user_id'].count()

# Unstack channel_age and transform it into a DataFrame
channel_age_df = pd.DataFrame(channel_age.unstack(level=1))


# Plot channel_age
channel_age_df.plot(kind='bar')
plt.title('Marketing channels by age group')
plt.xlabel('Age Group')
plt.ylabel('Users')
# Add a legend to the plot
plt.legend(loc='upper right', labels=channel_age_df.columns.values)
plt.show()

