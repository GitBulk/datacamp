'''
INTRODUCTION:
Calculating retention rate
In this exercise, you will calculate the retention rate, or the number of remaining subscribers from the users who converted to
your product. This can give you a sense of whether your marketing campaign converted subscribers who were actually interested in the product.

Conversion rate and retention rate function hand-in-hand; you could create a business with a high conversion rate by giving users
a free trial, but have a low retention rate once users are charged for your services. This isn't inherently a bad thing, but it is
important to provide your business stakeholders with insight into what percentage of users remain subscribers.

The formula for retention rate is:
N = Number of people who remain subscribed / Total number of people who converted


INTRUCTION:
Calculate the number of subscribers using the user_id and converted columns in the marketing DataFrame.
Calculate the number of retained subscribers using the boolean columns user_id and is_retained.
Calculate the retention rate.
'''

# Calculate the number of subscribers
total_subscribers = marketing[marketing['converted'] == True]['user_id'].nunique()

# Calculate the number of people who remained subscribed
retained = marketing[marketing['is_retained'] == True]['user_id'].nunique()

# Calculate the retention rate
retention_rate = retained / total_subscribers
print(round(retention_rate*100, 2), "%")

