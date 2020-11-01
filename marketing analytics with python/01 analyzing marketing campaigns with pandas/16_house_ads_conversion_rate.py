'''
INTRODUCTION:
House ads conversion rate
The house ads team has become worried about some irregularities they've noticed in conversion rate. It is common for stakeholders to
come to you with concerns they've noticed around changing metrics. As a data scientist, it's your job to determine whether these
changes are natural fluctuations or if they require further investigation.

In this exercise, you'll try out your conversion_rate() and plotting_conv() functions out on marketing looking at conversion rate
by 'date_served' and 'marketing_channel'.


INTRUCTION:
Use your conversion_rate() function on marketing to determine conversion rate by 'date_served' and 'marketing_channel'.
'''


# Calculate conversion rate by date served and channel
daily_conv_channel = conversion_rate(marketing, ['date_served', 'marketing_channel'])

print(daily_conv_channel.head())

# Unstack daily_conv_channel and convert it to a DataFrame
daily_conv_channel = pd.DataFrame(daily_conv_channel.unstack(level=1))

# Plot results of daily_conv_channel
plotting_conv(daily_conv_channel)
