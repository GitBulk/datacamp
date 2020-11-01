'''
INTRODUCTION:
Test and visualize conversion function
You've done the hard work of building your conversion rate function—now it's time to test it out! Automating your analyses
can be time-consuming up front, but this is where it all pays off.

In this exercise, you'll see how quickly you can calculate the conversion rate. A task that in previous lessons took multiple
steps. By automating the repetitive parts of your work, you'll be able to spend more time doing complex analyses.

INTRUCTION:
Use your conversion_rate() function to calculate the conversion rate in marketing by date_served and age_group and
store your results in age_group_conv.
Unstack age_group_conv at level equal to 1 and wrap that in a call to pd.DataFrame() to create age_group_df.
Create a line chart to display your results from age_group_df.
'''

# Calculate conversion rate by age_group
age_group_conv = conversion_rate(marketing, ['date_served', 'age_group'])
print(age_group_conv)

# Unstack and create a DataFrame
age_group_df = pd.DataFrame(age_group_conv.unstack(level=1))

# Visualize conversion by age_group
age_group_df.plot()
plt.title('Conversion rate by age group\n', size = 16)
plt.ylabel('Conversion rate', size = 14)
plt.xlabel('Age group', size = 14)
plt.show()



