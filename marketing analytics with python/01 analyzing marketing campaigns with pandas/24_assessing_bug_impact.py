'''
INTRODUCTION:
Assessing bug impact
It's time to calculate how many subscribers were lost due to mistakenly serving users English rather than their
preferred language. Once the team has an estimate of the impact of this error, they can determine whether it's
worth putting additional checks in place to avoid this in the future—you might be thinking, of course, it's worth
it to try to prevent errors! In a way, you're right, but every choice a company makes requires work and funding.
The more information your team has, the better they will be able to evaluate this trade-off.

The DataFrame converted has already been loaded for you. It contains expected subscribers columns for Spanish,
Arabic and German language speakers named expected_spanish_conv, expected_arabic_conv and expected_german_conv
respectively.


INTRUCTION:
Create the converted DataFrame by using .loc to select only rows where the date is between '2018-01-11' and '2018-01-31'.
Sum the expected subscribers columns for each language in converted and store the results in expected_subs.
Sum the actual subscribers for each language in converted and store the results in actual_subs.
Subtract actual_subs from expected_subs to determine how many subscribers were lost due to the bug.
'''

# Use .loc to slice only the relevant dates
converted = converted.loc['2018-01-11':'2018-01-31']

# Sum expected subscribers for each language
expected_subs = converted['expected_spanish_conv'].sum() + converted['expected_arabic_conv'].sum() + converted['expected_german_conv'].sum()

# Calculate how many subscribers we actually got
actual_subs = converted[('converted', 'Arabic')].sum() + converted[('converted', 'Spanish')].sum() + converted[('converted', 'German')].sum()

# Subtract how many subscribers we got despite the bug
lost_subs = expected_subs - actual_subs
print(lost_subs)
