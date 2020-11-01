'''
INTRODUCTION:
Plotting function
Now that you've looked at conversion rate by age, you want to see if that trend has changed over time. Marketing has been changing
their strategy and wants to make sure that their new method isn't alienating age groups that are less comfortable with their product.
However, to do so, you need to create a plotting function to make it easier to visualize your results.

In this exercise, you will build a function to plot the results of your conversion rate function.

INTRUCTION:
Create a for loop for each column in the dataframe.
Plot a line chart of the column by the DataFrame's index.
Show the plot.
'''
def plotting_conv(dataframe):
    for column in dataframe:
    # Plot column by dataframe's index
    plt.plot(dataframe.index, dataframe[column])
    plt.title('Daily ' + str(column) + ' conversion rate\n',
                size = 16)
    plt.ylabel('Conversion rate', size = 14)
    plt.xlabel('Date', size = 14)
    # Show plot
    plt.show()
    plt.clf()


