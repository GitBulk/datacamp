'''
INTRODUCTION:
Marketing channels across age groups
Some marketing stakeholders want to know if their marketing channels are reaching all users equally or if some marketing channels
are serving specific age demographics.

Within a marketing team, it is common to get requests that require quick analysis and visualization. The better you are at visualizing
the results, the more likely that you will effectively communicate your findings to your stakeholders.

In this exercise, you will create a grouped bar chart showing how many people each marketing channel reached by age group.


INTRUCTION:
Unstack channel_age with level = 1 and transform the result into a DataFrame.
Plot channel_age as a grouped bar chart.
Add a legend in the upper right and set the labels equal to channel_age_df.columns.values.
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



