'''
INTRODUCTION:
Building a conversion function
You've been doing a lot of repetitive calculations. Anytime you notice repetition in your work, consider automation. The more of the
low-variance work you can automate, the more time you will have to explore new and interesting data science topics at work. This will
both impress your marketing stakeholders and be more fun!

Since you know the format of the marketing DataFrame will remain the same over time, you can build a function to enable you to calculate
conversion rate across any sub-segment you want on the fly.

In this exercise, you will build a function that takes a DataFrame and list of column names and outputs the conversion rate across the column(s).

INTRUCTION:
Isolate rows in the user inputted dataframe where users were converted, then group by the list of user inputted column_names and count
the number of unique converted users.
Group the user inputted dataframe by the list of user inputted column_names and calculate the total number of users.
Fill any missing values in conversion_rate with 0.
'''
def conversion_rate(dataframe, column_names):
    # Total number of converted users
    column_conv = dataframe[dataframe['converted'] == True]\
                       .groupby(column_names)['user_id'].nunique()

    # Total number users
    column_total = dataframe.groupby(column_names)['user_id'].nunique()

    # Conversion rate
    conversion_rate = column_conv/column_total

    # Fill missing values with 0
    conversion_rate = conversion_rate.fillna(0)
    return conversion_rate

