'''
The subset of the data set containing the Iris versicolor petal lengths in units of centimeters (cm) is stored in
the NumPy array versicolor_petal_length.
'''


# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
plt.hist(versicolor_petal_length)

# Show histogram
plt.show()