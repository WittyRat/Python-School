"""#30NitesOfCode is a feature on Codédex that encourages one to code every day for a month.

A learner completed the challenge and recorded the amount of time they coded every single day for four weeks:

month_results = np.array([56, 100, 33, 0, 45, 45, 46, 34, 89, 180, 60, 45, 45, 44, 46, 45, 0, 0, 15, 90, 301, 197, 20, 60, 45, 45, 42, 45]) 

Without typing any code, what is the shape of this array? Confirm by using the .shape property.

Suppose we want to split this monthly data into weekly data. Use .reshape() so that each row is made of 7 items (for each week of the month)."""
import numpy as np

month_results = np.array([56, 100, 33, 0, 45, 45, 46, 34, 89, 180, 60, 45, 45, 44, 46, 45, 0, 0, 15, 90, 301, 197, 20, 60, 45, 45, 42, 45])

print(np.shape(month_results))
new_shape = month_results.reshape(4, 7)
print(new_shape)
