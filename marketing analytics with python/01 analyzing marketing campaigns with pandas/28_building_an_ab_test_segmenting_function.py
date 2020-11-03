'''
INTRODUCTION:
Creating a lift function
Lift can be calculated by calculating the difference between the treatment effect (or the mean) of the treatment compared to the treatment
effect of the control divided by the treatment effect of the control. The formula for lift can be found below:

N = (Treatment conversion rate - Control conversion rate) / Control conversion rate
The result is the percent difference between the control and treatment.

In this exercise, you will create a function to automate the process of calculating lift. Many marketing teams run tests constantly.
The more that you can automate the parts of the process that occur within every test, the more time you will have to do more interesting analyses.


INTRUCTION:
Calculate the mean of a and b using np.mean().
Use a_mean and b_mean to calculate the lift of the treatment.
Print the results of the lift() function you created using the control and personalization variables.
'''

def lift(a,b):
    # Calcuate the mean of a and b
    a_mean = np.mean(a)
    b_mean = np.mean(b)

    # Calculate the lift using a_mean and b_mean
    lift = (b_mean - a_mean) / a_mean

    return str(round(lift*100, 2)) + '%'

# Print lift() with control and personalization as inputs
print(lift(control, personalization))
