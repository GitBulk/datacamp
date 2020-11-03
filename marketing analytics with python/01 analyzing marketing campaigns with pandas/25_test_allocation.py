'''
INTRODUCTION:
Test allocation
The email portion of this campaign was actually run as an A/B test. Half the emails sent out were generic upsells to your product
while the other half contained personalized messaging around the users’ usage of the site.

Before you begin analyzing the results, you will check to ensure users were allocated equally to the test and control groups.


INTRUCTION:
Isolate the rows of marketing where the 'marketing_channel' is 'Email' and store the results in email.
Group marketing by variant and sum the unique users and store the results in alloc.
Plot the results of alloc in a bar chart.
'''

# Subset the DataFrame
email = marketing[marketing['marketing_channel'] == 'Email']

# Group the email DataFrame by variant
alloc = email.groupby('variant')['user_id'].nunique()

# Plot a bar chart of the test allocation
alloc.plot(kind='bar')
plt.title('Personalization test allocation')
plt.ylabel('# participants')
plt.show()
