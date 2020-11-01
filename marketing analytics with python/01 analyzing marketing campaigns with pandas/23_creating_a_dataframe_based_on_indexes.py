'''
INTRODUCTION:
Creating a DataFrame based on indexes
Now that you've created an index to compare English conversion rates against all other languages, you will build
out a DataFrame that will estimate what daily conversion rates should have been if users were being served the
correct language.

An expected conversion DataFrame named converted has been created for you grouping house_ads by date and preferred
language. It contains a count of unique users as well as the number of conversions for each language, each day.

For example, you can access the number of Spanish-speaking users who received house ads using
converted[('user_id','Spanish')].


INTRUCTION:
Use .loc to create the column english_conv_rate in converted with the English conversion rate between '2018-01-11' and '2018-01-31'.
Create expected conversion columns for each language by multiplying english_conv_rate by each language index (spanish_index, arabic_index or german_index).
Multiply each language's expected conversion rate by the number of users who should have received house ads.
'''
# Create English conversion rate column for affected period
converted['english_conv_rate'] = converted.loc['2018-01-11':'2018-01-31'][('converted','English')]

# Create expected conversion rates for each language
converted['expected_spanish_rate'] = converted['english_conv_rate']*spanish_index
converted['expected_arabic_rate'] = converted['english_conv_rate']*arabic_index
converted['expected_german_rate'] = converted['english_conv_rate']*german_index

# Multiply number of users by the expected conversion rate
converted['expected_spanish_conv'] = converted['expected_spanish_rate']/100*converted[('user_id','Spanish')]
converted['expected_arabic_conv'] = converted['expected_arabic_rate']/100*converted[('user_id','Arabic')]
converted['expected_german_conv'] = converted['expected_german_rate']/100*converted[('user_id','German')]

