'''
INTRODUCTION:
Visualize conversion rate by language
When you calculated conversion rate by age group in the previous exercise, you printed out a DataFrame called
language_conversion_rate containing your results. While this table provided useful information, it is much easier
to compare relative conversion rates visually.

It is critical for data scientists to communicate results clearly to business stakeholders. A strong foundation
in data visualization is a key aspect to conveying results, especially when engaging with people who are not
as comfortable interpreting data on their own.

In this exercise, you will build upon the work you did to create language_conversion_rate by visualizing your
results in a bar chart.


INTRUCTION:
Create a bar chart using the language_conversion_rate DataFrame.
Add the title 'Conversion rate by language\n' to your chart with font size 16.
Add an x-axis label, 'Language', and a y-axis label, 'Conversion rate (%)', both with font size 14.
Display the plot.
'''

# Create a bar chart using language_conversion_rate DataFrame
language_conversion_rate.plot(kind='bar')

# Add a title and x and y-axis labels
plt.title('Conversion rate by language\n', size = 16)
plt.ylabel('Conversion rate (%)', size = 14)
plt.xlabel('Language', size = 14)

# Display the plot
plt.show()
