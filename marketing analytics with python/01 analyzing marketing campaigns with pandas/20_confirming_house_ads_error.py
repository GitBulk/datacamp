'''
INTRODUCTION:
Confirming house ads error
Now that you've created a DataFrame that checks whether users see ads in the correct language let's calculate what percentage of users
were not being served ads in the right language and plot your results.

INTRUCTION:
Add a pct column to language_check_df which divides the count where language is correct by the row sum extracted using the .sum() method.
Make a line plot with the date as the x-axis and the pct column as the y-axis and show your results.
'''


# Divide the count where language is correct by the row sum
language_check_df['pct'] = language_check_df['Yes']/language_check_df.sum(axis=1)

# Plot and show your results
plt.plot(language_check_df.index.values, language_check_df['pct'])
plt.show()