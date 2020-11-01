'''
INTRODUCTION:
Visualize daily conversion rate
Now that your formatted the data into a more manageable format for visualization, you will proceed to create a line chart. Strong visualization
skills are crucial for a data scientist because it will allow you and your marketing stakeholders to derive deeper insights from the data.
In this case, creating a line plot will make it much easier to notice peaks and valleys in our conversion rate over time as well as any
overall trends.


INTRUCTION:
Create a line chart using the daily_conversion_rate DataFrame.
Set the y-axis of your chart to begin at 0.
Display the chart.
'''

# Create a line chart using daily_conversion_rate
daily_conversion_rate.plot('date_subscribed', 'conversion_rate')

plt.title('Daily conversion rate\n', size = 16)
plt.ylabel('Conversion rate (%)', size = 14)
plt.xlabel('Date', size = 14)

# Set the y-axis to begin at 0
plt.ylim(0)  # this line

# Display the plot
plt.show()
